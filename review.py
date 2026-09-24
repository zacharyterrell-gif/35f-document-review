import re
from pathlib import Path


def find_dates(text):
    """Find a few common written date formats."""
    patterns = [
        r"\b\d{4}-\d{2}-\d{2}\b",             # 2026-09-24
        r"\b\d{1,2}/\d{1,2}/\d{2,4}\b",        # 9/24/2026
        r"\b(?:January|February|March|April|May|June|July|August|"
        r"September|October|November|December) \d{1,2},? \d{4}\b",
    ]

    matches = []
    for pattern in patterns:
        matches.extend(re.findall(pattern, text, flags=re.IGNORECASE))

    return sorted(set(matches))


def find_relevant_sentences(text, keywords):
    """Return sentences containing at least one selected keyword."""
    sentences = re.split(r"(?<=[.!?])\s+|\n+", text)
    results = []

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue

        found = [
            word for word in keywords
            if word.lower() in sentence.lower()
        ]

        if found:
            results.append((sentence, found))

    return results


def make_report(title, text, keywords):
    dates = find_dates(text)
    hits = find_relevant_sentences(text, keywords)

    lines = [
        f"# Document Review: {title}",
        "",
        "## Source details — fill in before using this review",
        "- Source/URL:",
        "- Publication date:",
        "- Accessed on:",
        "- Classification/handling check:",
        "",
        "## Possible dates found",
    ]

    if dates:
        lines.extend(f"- {date}" for date in dates)
    else:
        lines.append("- None found by this simple date search.")

    lines.extend(["", "## Sentences to examine"])

    if hits:
        for number, (sentence, found) in enumerate(hits, start=1):
            lines.append(f"{number}. **Terms:** {', '.join(found)}")
            lines.append(f"   **Text:** {sentence}")
    else:
        lines.append("- No sentences matched your terms.")

    lines.extend([
        "",
        "## Analyst worksheet — complete yourself",
        "- **BLUF:**",
        "- **What the source directly says:**",
        "- **What I assess, and why:**",
        "- **Alternative explanation:**",
        "- **Confidence and information gaps:**",
        "- **What I would check next:**",
        "",
        "Automated matches are leads to verify against the original source.",
    ])

    return "\n".join(lines)


def main():
    print("35F Document Review Assistant")
    print("Practice with invented or explicitly approved unclassified text.")
    print()

    title = input("Document title: ").strip() or "Untitled document"

    terms = input(
        "Keywords, separated by commas "
        "(example: movement, supply, exercise): "
    )
    keywords = [word.strip() for word in terms.split(",") if word.strip()]

    if not keywords:
        keywords = ["movement", "supply", "exercise"]

    print()
    print("Paste the document text below.")
    print("When finished, type END on a line by itself and press Enter:")

    document_lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        document_lines.append(line)

    text = "\n".join(document_lines).strip()

    if not text:
        print("No document text was entered. Nothing was saved.")
        return

    report = make_report(title, text, keywords)

    print("\n" + "=" * 50)
    print(report)
    print("=" * 50)

    output_file = Path("review_output.md")
    output_file.write_text(report, encoding="utf-8")
    print(f"\nSaved your review to {output_file}")


if __name__ == "__main__":
    main()

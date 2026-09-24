# 35f-document-review 
# Document Review Workbench
A Python and Streamlit application for reviewing public or fictional documents.

## Features

- Upload one or two TXT, searchable PDF, or DOCX files 
- Find dates and selected search terms 
- See matching passages with source locations
- Compare data strings found in two documents 
- Write an analyst assessment and download a Markdown report 

## Run in GitHub Codespaces 

1. Run 'python -m pip install -r requirements.txt'
2. Run 'python -m streamlit run app.py'
3. Open the forwarded app in your browser
4. Upload fictional or explicitly approved public documents

## Limitations 

Matches are leads for human review. Different dates do not automatically mean two sources disagree. Scanned PDFs without electable text are not supported.

Do not upload classified information, CUI, restricted reportin, or personal data. 
This is an independent portfolio project, not an Army-approved system.
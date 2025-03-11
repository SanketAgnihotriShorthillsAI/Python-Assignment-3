# Document Data Extraction and Storage System

This project is a Python-based system designed to extract text, links, images, and tables from various document formats (PDF, DOCX, PPTX) and store the extracted data in files or an SQL database.

## 📂 Project Structure

📂 project_root/ │── 📂 data/ # Sample files for testing │ ├── sample.pdf │ ├── sample.docx │ ├── sample.pptx│──
📂 src/ │ ├── 📂 extractors/ # Data extraction module │ │ ├── data_extractor.py │ ├── 📂 loaders/ # File loading module │ │ ├── file_loader.py │ │ ├── pdf_loader.py │ │ ├── docx_loader.py │ │ ├── ppt_loader.py │
├── 📂 storage/ # Data storage module │ │ ├── file_storage.py │ │ ├── sql_storage.py │── test_script.py # Unit tests for modules │── .gitignore # Git ignore rules │── README.md # Project documentation

## Features
- **File Loaders**: Load content from PDF, DOCX, and PPT files.
- **Data Extraction**: Extract text, links, images, and tables.
- **Storage**: Save extracted data in a text file or SQLite database.
- **Unit Testing**: Ensures functionality across all modules.

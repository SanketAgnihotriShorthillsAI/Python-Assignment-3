# Document Data Extraction and Storage System

## Overview
This project provides a modular Python solution for extracting text, links, images, and tables from PDF, DOCX, and PPT files. The extracted data can be stored in a file or an SQLite database.

## Folder Structure
```
📂 project_root/
|—— 📂 data/                   # Sample files for testing
|   ├── sample.pdf
|   ├── sample.docx
|   ├── sample.pptx
|—— 📂 src/
|   ├── 📂 extractors/         # Data extraction module
|   |   ├── data_extractor.py
|   ├── 📂 loaders/            # File loading module
|   |   ├── file_loader.py
|   |   ├── pdf_loader.py
|   |   ├── docx_loader.py
|   |   ├── ppt_loader.py
|   ├── 📂 storage/            # Data storage module
|   |   ├── file_storage.py
|   |   ├── sql_storage.py
|—— test_script.py             # Unit tests for modules
|—— .gitignore                 # Git ignore rules
|—— README.md                  # Project documentation
```

## Features
- **File Loaders**: Load content from PDF, DOCX, and PPT files.
- **Data Extraction**: Extract text, links, images, and tables.
- **Storage**: Save extracted data in a text file or SQLite database.
- **Unit Testing**: Ensures functionality across all modules.

## Installation
1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd project_root
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Ensure test files exist in the `data/` directory.

## Usage
### Extracting Data
```python
from src.loaders.pdf_loader import PDFLoader
from src.extractors.data_extractor import DataExtractor

pdf_loader = PDFLoader("data/sample.pdf")
extractor = DataExtractor(pdf_loader)

text = extractor.extract_text()
links = extractor.extract_links()
images = extractor.extract_images()
tables = extractor.extract_tables()
```

### Storing Extracted Data
#### File Storage
```python
from src.storage.file_storage import FileStorage

file_storage = FileStorage(extractor)
file_storage.save_data()
```
#### SQL Storage
```python
from src.storage.sql_storage import SQLStorage

sql_storage = SQLStorage("data_store.sqlite", extractor)
sql_storage.save_data()
```

## Running Tests
To run the unit tests, execute:
```sh
python -m unittest test_script.py
```

## Author
Sanket Agnihotri
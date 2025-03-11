import sqlite3
from typing import Optional
from src.extractors.data_extractor import DataExtractor
from src.loaders.docx_loader import DOCXLoader
from src.loaders.pdf_loader import PDFLoader
from src.loaders.ppt_loader import PPTLoader


class SQLStorage:
    """
    Handles storage of extracted data into an SQLite database.
    """

    def __init__(self, db_name: str, extractor: DataExtractor) -> None:
        """
        Initializes the SQL storage with a database file and creates necessary tables.

        :param db_name: Name of the SQLite database file.
        :param extractor: An instance of DataExtractor for extracting data.
        """
        self.db_name = db_name
        self.extractor = extractor
        self.conn = sqlite3.connect(self.db_name)  # Connect to the SQLite database
        self.cursor = self.conn.cursor()
        self._create_tables()  # Ensure required tables exist

    def _create_tables(self) -> None:
        """
        Creates necessary tables if they do not exist in the database.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS text_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS links (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS images (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data BLOB
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tables (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT
            )
        """)
        self.conn.commit()  # Save changes

    def save(self) -> None:
        """
        Extracts and stores text, links, images, and tables in the database.
        """
        try:
            text_data: Optional[str] = self.extractor.extract_text()
            links = self.extractor.extract_links()
            images = self.extractor.extract_images()
            tables = self.extractor.extract_tables()

            # Save extracted text
            if text_data:
                self.cursor.execute("INSERT INTO text_data (content) VALUES (?)", (text_data,))
                print("Text saved successfully.")

            # Save extracted links
            for link in links:
                self.cursor.execute("INSERT INTO links (url) VALUES (?)", (link,))
            print("Links saved successfully.")

            # Save extracted images
            for idx, img in enumerate(images):
                if isinstance(img, bytes):  # Ensure the image is in binary format
                    self.cursor.execute("INSERT INTO images (data) VALUES (?)", (sqlite3.Binary(img),))
                    print(f"Image {idx} saved successfully.")
                else:
                    print(f"Skipped image {idx} - Invalid format.")

            # Save extracted tables
            for idx, table in enumerate(tables):
                table_str = str(table)  # Convert table to string format before saving
                self.cursor.execute("INSERT INTO tables (content) VALUES (?)", (table_str,))
                print(f"Table {idx} saved successfully.")

            self.conn.commit()  # Commit changes to database
            print("All extracted data has been saved to the database successfully!")

        except Exception as e:
            print(f"Error saving data to database: {e}")

    def close(self) -> None:
        """
        Closes the database connection.
        """
        self.conn.close()
        print("Database connection closed.")


# Example Usage: Store extracted data from DOCX, PDF, and PPTX

print("\nProcessing DOCX file...")
docx_test = SQLStorage("test_db.sqlite", DataExtractor(DOCXLoader("data/sample.docx")))
docx_test.save()
docx_test.close()

# print("\nProcessing PDF file...")
# pdf_test = SQLStorage("test_db.sqlite", DataExtractor(PDFLoader("sample.pdf")))
# pdf_test.save()
# pdf_test.close()

# print("\nProcessing PPT file...")
# ppt_test = SQLStorage("test_db.sqlite", DataExtractor(PPTLoader("sample.pptx")))
# ppt_test.save()
# ppt_test.close()

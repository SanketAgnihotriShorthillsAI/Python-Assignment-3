import unittest
from src.loaders.pdf_loader import PDFLoader
from src.loaders.docx_loader import DOCXLoader
from src.loaders.ppt_loader import PPTLoader
from src.extractors.data_extractor import DataExtractor
from src.storage.file_storage import FileStorage
from src.storage.sql_storage import SQLStorage

class TestFileLoaders(unittest.TestCase):

    def setUp(self):
        """Setup test files for each format"""
        self.pdf_loader = PDFLoader("data/sample.pdf")
        self.docx_loader = DOCXLoader("data/sample.docx")
        self.ppt_loader = PPTLoader("data/sample.pptx")

    def test_pdf_loading(self):
        """Test if the PDF loader correctly loads a file"""
        self.assertIsNotNone(self.pdf_loader.load_file(), "PDF file should load successfully")

    def test_docx_loading(self):
        """Test if the DOCX loader correctly loads a file"""
        self.assertIsNotNone(self.docx_loader.load_file(), "DOCX file should load successfully")

    def test_ppt_loading(self):
        """Test if the PPT loader correctly loads a file"""
        self.assertIsNotNone(self.ppt_loader.load_file(), "PPT file should load successfully")


class TestDataExtractor(unittest.TestCase):

    def setUp(self):
        """Initialize DataExtractor with different loaders"""
        self.pdf_loader = PDFLoader("data/sample.pdf")
        self.extractor_pdf = DataExtractor(self.pdf_loader)

        self.docx_loader = DOCXLoader("data/sample.docx")
        self.extractor_docx = DataExtractor(self.docx_loader)

        self.ppt_loader = PPTLoader("data/sample.pptx")
        self.extractor_ppt = DataExtractor(self.ppt_loader)

    def test_extract_text(self):
        """Test text extraction from different file types"""
        self.assertIsInstance(self.extractor_pdf.extract_text(), str, "Text extraction should return a string")
        self.assertIsInstance(self.extractor_docx.extract_text(), str, "Text extraction should return a string")
        self.assertIsInstance(self.extractor_ppt.extract_text(), str, "Text extraction should return a string")

    def test_extract_links(self):
        """Test if links are extracted properly"""
        self.assertIsInstance(self.extractor_pdf.extract_links(), list, "Links should be returned as a list")
        self.assertIsInstance(self.extractor_docx.extract_links(), list, "Links should be returned as a list")
        self.assertIsInstance(self.extractor_ppt.extract_links(), list, "Links should be returned as a list")

    def test_extract_images(self):
        """Test if images are extracted properly"""
        self.assertIsInstance(self.extractor_pdf.extract_images(), list, "Images should be returned as a list")
        self.assertIsInstance(self.extractor_docx.extract_images(), list, "Images should be returned as a list")
        self.assertIsInstance(self.extractor_ppt.extract_images(), list, "Images should be returned as a list")

    def test_extract_tables(self):
        """Test if tables are extracted properly"""
        self.assertIsInstance(self.extractor_pdf.extract_tables(), list, "Tables should be returned as a list")
        self.assertIsInstance(self.extractor_docx.extract_tables(), list, "Tables should be returned as a list")
        self.assertIsInstance(self.extractor_ppt.extract_tables(), list, "Tables should be returned as a list")


class TestStorage(unittest.TestCase):

    def setUp(self):
        """Setup storage instances with mock extractors"""
        self.pdf_loader = PDFLoader("data/sample.pdf")
        self.extractor = DataExtractor(self.pdf_loader)

        self.file_storage = FileStorage(self.extractor)
        self.sql_storage = SQLStorage("test_db.sqlite", self.extractor)

    def test_file_storage(self):
        """Test if data is correctly stored in a file"""
        result = self.file_storage.save_data()
        self.assertTrue(result, "Data should be stored in a file successfully")

    def test_sql_storage(self):
        """Test if data is correctly stored in SQL database"""
        result = self.sql_storage.save()
        self.assertTrue(result, "Data should be stored in SQL database successfully")


if __name__ == "__main__":
    unittest.main()

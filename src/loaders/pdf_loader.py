from src.loaders.file_loader import FileLoader
import fitz  # PyMuPDF

class PDFLoader(FileLoader):
    """
    Concrete class for loading PDF files.
    
    This class validates and loads a PDF file using PyMuPDF (fitz).
    """

    def __init__(self, file_path: str) -> None:
        """
        Initialize the PDFLoader with a file path.

        :param file_path: Path to the PDF file.
        """
        super().__init__(file_path)  # Call parent constructor

    def validate_file(self) -> bool:
        """
        Validate if the file is a proper PDF format.

        :return: True if the file is a valid PDF, False otherwise.
        """
        return self.file_path.lower().endswith(".pdf")  # Simple format check

    def load_file(self) -> fitz.Document | None:
        """
        Loads the PDF file and returns a PyMuPDF document object.

        :return: A fitz.Document object if successful, else None.
        """
        try:
            document = fitz.open(self.file_path)  # Open PDF file
            print("PDF successfully loaded")
            return document
        except Exception as e:
            print(f"Error loading PDF: {e}")  # Handle exceptions gracefully
            return None

        
# test = PDFLoader("data/sample.pdf")
# print(test.load_file())
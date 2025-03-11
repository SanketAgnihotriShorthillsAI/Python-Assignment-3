# DOCX Loader

from src.loaders.file_loader import FileLoader
import docx
from docx.document import Document


class DOCXLoader(FileLoader):
    """
    Concrete class for loading DOCX files.

    This class validates and loads a DOCX file using python-docx.
    """

    def __init__(self, file_path: str) -> None:
        """
        Initialize the DOCXLoader with a file path.

        :param file_path: Path to the DOCX file.
        """
        super().__init__(file_path)  # Call parent constructor

    def validate_file(self) -> bool:
        """
        Validate if the file is a proper DOCX format.

        :return: True if the file is a valid DOCX, False otherwise.
        """
        return self.file_path.lower().endswith(".docx")  # Simple format check

    def load_file(self) -> Document | None:
        """
        Loads the DOCX file and returns a python-docx document object.

        :return: A Document object if successful, else None.
        """
        try:
            document = docx.Document(self.file_path)  # Open DOCX file
            print("DOCX successfully loaded")
            return document
        except Exception as e:
            print(f"Error loading DOCX: {e}")  # Handle exceptions gracefully
            return None


# test = DOCXLoader("data/sample.docx")
# print(test.load_file())


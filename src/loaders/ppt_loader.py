# PPT Loader

from .file_loader import FileLoader

from pptx import Presentation
import os

class PPTLoader:
    def __init__(self, file_path):
        """Loads and processes a PPTX file."""
        self.file_path = file_path
        self.document = self.load_file()

    def load_file(self):
        """Loads a PPTX file, ensuring it exists before processing."""
        if not os.path.exists(self.file_path):
            print(f"Error: PPT file '{self.file_path}' not found! Please check the path.")
            return None  # Return None instead of crashing
        
        if not self.file_path.endswith(".pptx"):
            print(f"Error: Unsupported file format '{self.file_path}'. Convert it to .pptx")
            return None

        try:
            return Presentation(self.file_path)  # Load the PPTX file
        except Exception as e:
            print(f"Error loading PPT: {e}")
            return None  # Handle corrupt files


        
# test = PPTLoader("data/sample.pptx")
# print(test.load_file())


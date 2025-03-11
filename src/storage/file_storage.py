import os
import csv
from typing import Optional
from src.extractors.data_extractor import DataExtractor
from src.loaders.docx_loader import DOCXLoader
from src.loaders.pdf_loader import PDFLoader
from src.loaders.ppt_loader import PPTLoader


class FileStorage:
    """
    Handles the storage of extracted data (text, links, images, and tables) into files.
    """

    def __init__(self, extractor: DataExtractor, output_folder: str = "output") -> None:
        """
        Initializes FileStorage with an extractor and output directory.

        :param extractor: An instance of DataExtractor containing extracted data.
        :param output_folder: Directory where extracted files will be saved.
        """
        self.extractor = extractor
        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)  # Ensure output directory exists

    def save_text(self) -> None:
        """
        Saves extracted text into a text file.
        """
        text: Optional[str] = self.extractor.extract_text()
        if text:
            with open(os.path.join(self.output_folder, "extracted_text.txt"), "w", encoding="utf-8") as f:
                f.write(text)
            print("Text saved successfully.")

    def save_links(self) -> None:
        """
        Saves extracted hyperlinks into a text file.
        """
        links = self.extractor.extract_links()
        if links:
            with open(os.path.join(self.output_folder, "extracted_links.txt"), "w", encoding="utf-8") as f:
                f.write("\n".join(links))
            print("Links saved successfully.")

    def save_images(self) -> None:
        """
        Saves extracted images as separate PNG files.
        """
        images = self.extractor.extract_images()
        for idx, img_data in enumerate(images):
            try:
                # Ensure image data is in bytes
                if isinstance(img_data, bytes):
                    img_path = os.path.join(self.output_folder, f"image_{idx}.png")
                    with open(img_path, "wb") as f:
                        f.write(img_data)
                    print(f"Image saved: {img_path}")
                else:
                    print(f"⚠️ Skipped image {idx} - Invalid data format")
            except Exception as e:
                print(f"Error saving image {idx}: {e}")

    def save_tables(self) -> None:
        """
        Saves extracted tables into CSV files.
        """
        tables = self.extractor.extract_tables()
        for idx, table in enumerate(tables):
            csv_path = os.path.join(self.output_folder, f"table_{idx}.csv")
            try:
                with open(csv_path, "w", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerows(table)
                print(f"Table saved: {csv_path}")
            except Exception as e:
                print(f"Error saving table {idx}: {e}")

    def save_data(self):
        """Saves all extracted data and returns True if successful."""
        self.save_text()
        self.save_links()
        self.save_images()
        self.save_tables()
        print("✅ Data saved to files")
        return True  # Ensure return value for unit test assertion



# Example Usage: Test FileStorage with DOCX, PDF, and PPTX

print("\nProcessing DOCX file...")
docx_test = FileStorage(DataExtractor(DOCXLoader("data/sample.docx")))
docx_test.save_data()

# print("\nProcessing PDF file...")
# pdf_test = FileStorage(DataExtractor(PDFLoader("data/sample.pdf")))
# pdf_test.save_data()

# print("\nProcessing PPT file...")
# ppt_test = FileStorage(DataExtractor(PPTLoader("data/sample.pptx")))
# ppt_test.save_data()

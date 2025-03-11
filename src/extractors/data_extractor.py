import io
from PIL import Image
from src.loaders.pdf_loader import PDFLoader
from src.loaders.docx_loader import DOCXLoader
from src.loaders.ppt_loader import PPTLoader
from typing import List, Union, Optional


class DataExtractor:
    """
    Extracts text, hyperlinks, images, and tables from various file formats.

    Supports:
    - PDFs using PyMuPDF
    - DOCX using python-docx
    - PPTX using python-pptx
    """

    def __init__(self, file_loader: Union[PDFLoader, DOCXLoader, PPTLoader]) -> None:
        """
        Initialize DataExtractor with a FileLoader instance.

        :param file_loader: An instance of PDFLoader, DOCXLoader, or PPTLoader.
        """
        self.file_loader = file_loader
        self.document = self.file_loader.load_file()

    def extract_text(self) -> Optional[str]:
        """
        Extracts text from the loaded document.

        :return: Extracted text as a string, or None if extraction fails.
        """
        if not self.document:
            return None

        # Extract text from PDF
        if isinstance(self.file_loader, PDFLoader):
            return "\n".join([page.get_text() for page in self.document])

        # Extract text from DOCX
        if isinstance(self.file_loader, DOCXLoader):
            return "\n".join([para.text for para in self.document.paragraphs])

        # Extract text from PPT
        if isinstance(self.file_loader, PPTLoader):
            return "\n".join(
                [shape.text for slide in self.document.slides for shape in slide.shapes if hasattr(shape, "text")]
            )

        return None

    def extract_links(self) -> List[str]:
        """
        Extracts hyperlinks from the loaded document.

        :return: A list of extracted hyperlinks.
        """
        links = []

        # Extract links from PDF
        if isinstance(self.file_loader, PDFLoader):
            for page in self.document:
                links.extend(page.get_links())  # Extracts hyperlinks from PDF

        # Extract links from DOCX
        elif isinstance(self.file_loader, DOCXLoader):
            for rel in self.document.part.rels.values():
                if "hyperlink" in rel.reltype:
                    links.append(rel.target_ref)  # Extract hyperlink reference

        # Extract links from PPT
        elif isinstance(self.file_loader, PPTLoader):
            for slide in self.document.slides:
                for shape in slide.shapes:
                    if hasattr(shape, "hyperlink") and shape.hyperlink.address:
                        links.append(shape.hyperlink.address)  # Extract hyperlink from shape

        return links  # Returns list of extracted hyperlinks

    def extract_images(self) -> List[bytes]:
        """
        Extracts images from the loaded document.

        :return: A list of extracted image byte data.
        """
        images = []

        # Extract images from PDF
        if isinstance(self.file_loader, PDFLoader):
            for page in self.document:
                for img in page.get_images(full=True):
                    xref = img[0]
                    base_image = self.document.extract_image(xref)
                    images.append(base_image["image"])  # Extract the image bytes

        # Extract images from DOCX
        elif isinstance(self.file_loader, DOCXLoader):
            for rel in self.document.part.rels.values():
                if "image" in rel.reltype:
                    image_part = self.document.part.rels[rel.rId].target_part
                    images.append(image_part.blob)  # Extract image as bytes

        # Extract images from PPT
        elif isinstance(self.file_loader, PPTLoader):
            for slide in self.document.slides:
                for shape in slide.shapes:
                    if hasattr(shape, "image"):
                        images.append(shape.image.blob)  # Extract image as bytes

        return images  # Returns list of images in bytes format

    def extract_tables(self) -> List[List[List[str]]]:
        """
        Extracts tables from the loaded document.

        :return: A list of tables, where each table is represented as a list of lists.
        """
        tables = []

        # Extract tables from DOCX
        if isinstance(self.file_loader, DOCXLoader):
            for table in self.document.tables:
                table_data = [[cell.text for cell in row.cells] for row in table.rows]
                tables.append(table_data)

        # Extract tables from PPT
        elif isinstance(self.file_loader, PPTLoader):
            for slide in self.document.slides:
                for shape in slide.shapes:
                    if hasattr(shape, "has_table") and shape.has_table:
                        table = shape.table  # Now safe to access
                        table_data = [[cell.text for cell in row.cells] for row in table.rows]
                        tables.append(table_data)

        return tables  # Returns a list of extracted tables



# pdf_extractor = DataExtractor(PDFLoader("data/sample.pdf"))
# print(pdf_extractor.extract_text())
# print(pdf_extractor.extract_links())
# print(pdf_extractor.extract_images())

# docx_extractor = DataExtractor(DOCXLoader("data/sample.docx"))
# print(docx_extractor.extract_text())
# print(docx_extractor.extract_links())
# print(docx_extractor.extract_images())

# ppt_extractor = DataExtractor(PPTLoader("data/sample.pptx"))
# print(ppt_extractor.extract_text())
# print(ppt_extractor.extract_links())
# print(ppt_extractor.extract_images())

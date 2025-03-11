from abc import ABC, abstractmethod

class FileLoader(ABC):
    """
    Abstract base class for file loading.

    This class defines a structure for all file loaders, ensuring 
    they implement validation and file-loading mechanisms.
    """

    def __init__(self, file_path: str) -> None:
        """
        Initialize the FileLoader with the given file path.

        :param file_path: Path to the file to be loaded.
        """
        self.file_path = file_path  # Store the file path

    @abstractmethod
    def validate_file(self) -> bool:
        """
        Validate the file format to ensure compatibility.

        :return: True if the file format is valid, False otherwise.
        """
        pass

    @abstractmethod
    def load_file(self):
        """
        Load the content of the file.

        :return: Loaded file data in an appropriate format.
        """
        pass

from abc import ABC, abstractmethod

class Storage(ABC):
    """Abstract class for storing extracted data."""

    @abstractmethod
    def save_data(self, data):
        pass

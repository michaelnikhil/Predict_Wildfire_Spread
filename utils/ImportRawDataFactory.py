from abc import ABC, abstractmethod

class importer(ABC):
    @staticmethod
    @abstractmethod
    def import_data(self):
        pass
from abc import ABC, abstractmethod

class worker(ABC):
    @abstractmethod
    def import_data(self):
        pass

    @abstractmethod
    def process_data(self, input_data):
        pass


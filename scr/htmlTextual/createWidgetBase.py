from abc import ABC, abstractmethod
from textual.widget import Widget

class CreateWidgetBase(ABC):
    @abstractmethod
    def create(self, attributes:dict) -> Widget:
        pass
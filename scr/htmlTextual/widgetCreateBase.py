from abc import ABC, abstractmethod
from textual.widget import Widget

class WidgetCreateBase(ABC):
    @abstractmethod
    def create(self, attributes:dict) -> Widget:
        pass
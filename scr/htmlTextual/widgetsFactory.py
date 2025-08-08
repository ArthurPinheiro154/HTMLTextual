from textual.widget import Widget
from .labelCreateWidget import LabelWidget
from .buttonCreateWidget import ButtonWidget
from .listItemCreateWidget import ListItemCreateWidget
from .listViewCreateWidget import ListViewCreateWidget

class WidgetsFactory:
    def create(self, widgetType:str, attributes:dict)->Widget:
        if widgetType == 'label':
            return LabelWidget().create(attributes)
        if widgetType == 'button':
            return ButtonWidget().create(attributes)
        if widgetType == 'listItem':
            return ListItemCreateWidget().create(attributes)
        if widgetType == 'listView':
            return ListViewCreateWidget().create(attributes)
        return None
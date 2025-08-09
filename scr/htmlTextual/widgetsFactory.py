from textual.widget import Widget
from .createLabelWidget import CreateLabelWidget
from .createButtonWidget import CreateButtonWidget
from .createListItemWidget import CreateListItemWidget
from .createListViewWidget import CreateListViewWidget
from .createInputWidget import CreateInputWidget
from .createCheckBoxWidget import CreateCheckBoxWidget

class WidgetsFactory:
    _widgetMap = {
        'label': CreateLabelWidget,
        'button': CreateButtonWidget,
        'listItem': CreateListItemWidget,
        'listView': CreateListViewWidget,
        'input': CreateInputWidget,
        'checkBox': CreateCheckBoxWidget
    }

    def create(self, widgetType:str, attributes:dict)->Widget:
        widgetClass = self._widgetMap.get(widgetType)
        if widgetClass:
            return widgetClass().create(attributes)
        return None
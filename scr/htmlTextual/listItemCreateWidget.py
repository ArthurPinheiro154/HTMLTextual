from .widgetCreateBase import WidgetCreateBase
from textual.widget import Widget
from textual.widgets import ListItem

class ListItemCreateWidget(WidgetCreateBase):
    def create(self, attributes:dict) -> Widget:
        return ListItem(
            attributes['children'],
            name=       attributes['name'],
            id=         attributes['id'],
            classes=    attributes['classes'],
            disabled=   attributes['disabled'],
            markup=     attributes['markup']
        )
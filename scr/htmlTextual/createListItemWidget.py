from .createWidgetBase import CreateWidgetBase
from textual.widget import Widget
from textual.widgets import ListItem

class CreateListItemWidget(CreateWidgetBase):
    def create(self, attributes:dict) -> Widget:
        return ListItem(
            attributes['children'],
            name=       attributes['name'],
            id=         attributes['id'],
            classes=    attributes['classes'],
            disabled=   attributes['disabled'],
            markup=     attributes['markup']
        )
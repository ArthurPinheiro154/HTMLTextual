from .createWidgetBase import CreateWidgetBase
from textual.widget import Widget
from textual.widgets import ListView

class CreateListViewWidget(CreateWidgetBase):
    def create(self, attributes:dict) -> Widget:
        return ListView(
            attributes['listItems'],
            initial_index=  attributes['initial_index'],
            name=           attributes['name'],
            id =            attributes['id'],
            classes=        attributes['classes'],
            disabled=       attributes['disabled']
        )
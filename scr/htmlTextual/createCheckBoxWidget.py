from .createWidgetBase import CreateWidgetBase
from textual.widgets import Checkbox
from textual.widget import Widget

class CreateCheckBoxWidget(CreateWidgetBase):
    def create(self, attributes:dict) -> Widget:
        return Checkbox(
            label=          attributes['label'],
            value=          attributes['value'],
            button_first=   attributes['button_first'],
            name=           attributes['name'],
            id=             attributes['id'],
            classes=        attributes['classes'],
            disabled=       attributes['disabled'],
            tooltip=        attributes['tooltip'],
            compact=        attributes['compact']
        )

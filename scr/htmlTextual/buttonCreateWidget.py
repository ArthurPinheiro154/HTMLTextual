from .widgetCreateBase import WidgetCreateBase
from textual.widget import Widget
from textual.widgets import Button

class ButtonWidget(WidgetCreateBase):
    def create(self, attributes:dict) -> Widget:
        return Button(
            label=      attributes['label'],
            variant=    attributes['variant'],
            name=       attributes['name'],
            id =        attributes['id'],
            classes=    attributes['classes'],
            disabled=   attributes['disabled'],
            tooltip=    attributes['tooltip'],
            action=     attributes['action'],
            compact=    attributes['compact']
        )
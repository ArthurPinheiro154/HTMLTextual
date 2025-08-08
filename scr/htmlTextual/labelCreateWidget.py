from .widgetCreateBase import WidgetCreateBase
from textual.widget import Widget
from textual.widgets import Label

class LabelWidget(WidgetCreateBase):
    def create(self, attributes:dict) -> Widget:
        return Label(
            renderable=attributes['renderable'],
            variant=attributes['variant'],
            expand=attributes['expand'],
            shrink=attributes['expand'],
            markup=attributes['markup'],
            name=attributes['name'],
            id=attributes['id'],
            classes=attributes['classes'],
            disabled=attributes['disabled']
        )
from .createWidgetBase import CreateWidgetBase
from textual.widgets import Input
from textual.widget import Widget

class CreateInputWidget(CreateWidgetBase):
    def create(self, attributes:dict) -> Widget:
        return Input(
            value=attributes['value'],
            placeholder=attributes['placeHolder'],
            highlighter=attributes['highlighter'],
            password=attributes['password'],
            restrict=attributes['restrict'],
            type=attributes['type'],
            max_length=attributes['max_length'],
            suggester=attributes['suggester'],
            validators=attributes['validators'],
            validate_on=attributes['validate_on'],
            valid_empty=attributes['valid_empty'],
            select_on_focus=attributes['select_on_focus'],
            name=attributes['name'],
            id=attributes['id'],
            classes=attributes['classes'],
            disabled=attributes['disabled'],
            tooltip=attributes['tooltip'],
            compact=attributes['compact']
        )

from .widgetsFactory import WidgetsFactory
from textual.app import App, ComposeResult

class test(App):
    def __init__(self, widgets:list):
        super().__init__()
        self.widgets = widgets

    def compose(self) -> ComposeResult:
        for widget in self.widgets:
            yield widget

def main():
    labelAtributes = {
        'renderable':   "Hello, World",
        'variant':      None,
        'expand':       False,
        'shrink':       False,
        'markup':       True,
        'name':         None,
        'id':           None,
        'classes':      None,
        'disabled':     False
    }

    buttonAtributes = {
        'label':        None,
        'variant':      'default',
        'name':         None,
        'id':           None,
        'classes':      None,
        'disabled':     False,
        'tooltip':      None,
        'action':       None,
        'compact':      False
    }

    fabric = WidgetsFactory()

    lable = fabric.create('label', labelAtributes)

    listItemAtributes = {
        'children':  lable,
        'name':      None,
        'id':        None,
        'classes':   None,
        'disabled':  False,
        'markup':    True
    }

    listItem = fabric.create('listItem', listItemAtributes)

    listViewAttributes = {
        'listItems':        listItem, 
        'initial_index':    0,
        'name':             None,
        'id':               None,
        'classes':          None,
        'disabled':         False
    }

    button = fabric.create('button', buttonAtributes)
    
    listView = fabric.create('listView', listViewAttributes)

    inputAttributes = {
        'value':            None, 
        'placeHolder':      "",
        'highlighter':      None,
        'password':         False,
        'restrict':         None,
        'type':             'text',
        'max_length':       0,
        'suggester':        None, 
        'validators':       None,
        'validate_on':      None,
        'valid_empty':      False,
        'select_on_focus':  True,
        'name':             None,
        'id':               None,
        'classes':          None,
        'disabled':         False,
        'tooltip':          None,
        'compact':          False
    }

    input = fabric.create('input', inputAttributes)

    app = test([lable, button, listView, input])
    app.run()

if __name__== '__main__':
    main()
from .item import Item

class Electronics(Item): 
    def __init__(self, type="Unknown", **kwargs):
        super().__init__(**kwargs) 
        self.type = type

    def __str__(self):
        item_string = super().__str__()
        return item_string + f" This is a {self.type} device."
        
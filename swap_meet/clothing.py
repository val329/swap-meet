from .item import Item

class Clothing(Item):
    def __init__(self, fabric="Unknown", **kwargs):
        super().__init__(**kwargs) 
        self.fabric = fabric

    def __str__(self):
        item_string = super().__str__()
        return item_string + f" It is made from {self.fabric} fabric."

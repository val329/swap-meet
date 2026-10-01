from .item import Item

class Decor(Item): 
    def __init__(self, width=0, length=0, **kwargs):
        super().__init__(**kwargs) 
        self.width = width
        self.length = length
        
    def __str__(self):
        item_string = super().__str__()
        return item_string + f" It takes up a {self.width} by {self.length} sized space."
    

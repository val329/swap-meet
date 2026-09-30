from .item import Item

FABRICS = ["Striped", "Cotton", "Floral"]

class Clothing(Item):
    def __init__(self, fabric="Unknown", **kwargs):
        super().__init__(**kwargs) 
        self.fabric = fabric

    def get_category(self):
        return "Clothing"

    def __str__(self):
        return f"An object of type Clothing with id {self.id}. "\
               f"It is made from {self.fabric} fabric."
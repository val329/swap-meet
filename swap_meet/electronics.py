from .item import Item

class Electronics(Item): 
    def __init__(self, type="Unknown", **kwargs):
        super().__init__(**kwargs) 
        self.type = type
        

    def get_category(self):
        return "Electronics"

    def __str__(self):
        return  f"An object of type Electronics with id {self.id}. "\
                f"This is a {self.type} device."
    
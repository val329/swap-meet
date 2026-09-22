import uuid

class Item:

    def __init__(self, id=None):
        if id:  
            self.id = id
        else: 
            self.id = uuid.uuid4().int

    def get_category(self):
        return "Item"

#Added for Wave3 to define how an Item return as a string
    def __str__(self):
        return f"An object of type Item with id {self.id}."


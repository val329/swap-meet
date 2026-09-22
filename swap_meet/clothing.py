import uuid
class Clothing:

    def __init__(self, id=None, fabric="Unknown"):
        if id is not None: 
            self.id = id
        else: 
            self.id = uuid.uuid4().int
        self.fabric = fabric

    def get_category(self):
        return "Clothing"

    def __str__(self):
        return f"An object of type Clothing with id {self.id}. "\
               f"It is made from {self.fabric} fabric."

class Decor: 
    def __init__(self, width=0, length=0):
        if id is not None: 
            self.id = id
        else: 
            self.id = uuid.uuid4().int
        self.width = width
        self.length = length

    def get_category(self):
        return "Decor"

    def __str__(self):
        return f"An object of type Decor with id {id}. "\
               f"It takes up a {self.width} by {self.length} sized space."


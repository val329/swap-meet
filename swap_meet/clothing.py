import uuid

class Clothing:
    def __init__(self, id=None, fabric="Unknown"):
        self.id = id if id is not None else uuid.uuid4().int
        self.fabric = fabric

    def get_category(self):
        return "Clothing"

    def __str__(self):
        return f"An object of type Clothing with id {self.id}. "\
               f"It is made from {self.fabric} fabric."
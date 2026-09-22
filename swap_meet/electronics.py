import uuid
from .item import Item

TYPES = ["Kitchen Appliance", "Game Console", "Health Tracker"]

class Electronics(Item): 
    def __init__(self, id=None, type="Unknown", condition=0):
        self.id = id if id is not None else uuid.uuid4().int
        self.type = type
        self.condition = condition

    def get_category(self):
        return "Electronics"

    def __str__(self):
        return  f"An object of type Electronics with id {self.id}. "\
                f"This is a {self.type} device."
    
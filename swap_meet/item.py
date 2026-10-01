import uuid

CONDITIONS = {
    0: "very not mint condition",
    1: "visibly used",
    2: "slightly used",
    3: "mint",
    4: "as new"
}

class Item:
    def __init__(self, id=None, condition=0.0, age=None):
        self.id = id if id is not None else uuid.uuid4().int
        self.condition = condition
        self.age = age

    def get_category(self):
        return self.__class__.__name__

    def condition_description(self):
        index = round(self.condition) - 1
        return CONDITIONS[index]

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
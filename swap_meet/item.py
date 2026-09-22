import uuid
CONDITIONS = ["very not mint condition", "visibly used", "slightly used", "mint", "as new"]

class Item:

    def __init__(self, id=None, condition=0):
        if id:  
            self.id = id
        else: 
            self.id = uuid.uuid4().int

    def get_category(self):
        return "Item"










    def condition_description(self):
        index = round(self.condition) - 1
        return CONDITIONS[index]




class Vendor:

    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return None
         
        self.inventory.remove(item)
        return item

    def get_by_id(self, id):
        for item in self.inventory: 
            if item.id == id: 
                return item

        return None

# Wave3 logic for self and other_vendor to swap items
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        self.remove(my_item)
        other_vendor.remove(their_item)

        self.add(their_item)
        other_vendor.add(my_item)
        return True

# Wave4 logic to swap the first item between self and other_vendor
    def swap_first_item(self, other_vendor):

        if not self.inventory or not other_vendor.inventory:
            return False
        
        return self.swap_items(
            other_vendor,
            self.inventory[0],
            other_vendor.inventory[0]
        )

# Added for Wave 6 to return all items that match a category
    def get_by_category(self, category):
        return [item for item in self.inventory if item.get_category() == category]

    def get_best_by_category(self, category):
        matching_items = self.get_by_category(category)

        if not matching_items:
            return None

        return max(matching_items, key=lambda item: item.condition)

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):

        if not self.inventory or not other_vendor.inventory: 
            return False

        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        if not my_best_item or not their_best_item: 
            return False
        self.swap_items(other_vendor, my_best_item, their_best_item)
        return True


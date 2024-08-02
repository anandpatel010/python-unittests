class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item: str, quantity: int):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item: str, quantity: int) -> bool:
        if item in self.items and self.items[item] >= quantity:
            self.items[item] -= quantity
            if self.items[item] == 0:
                del self.items[item]
            return True
        return False

    def get_inventory(self) -> dict:
        return self.items

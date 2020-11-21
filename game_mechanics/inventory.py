from items.items import Items


class Inventory:
    def __init__(self):
        self.inside = []

    def add_item(self, item):
        if isinstance(item, Items):
            self.inside.append(item)

    def find_item(self, item_name):
        for item in self.inside:
            if item.name == item_name:
                return item

    def rem_item(self, item_name):
        for item in self.inside:
            if item.name == item_name:
                self.inside.remove(item)

    def check(self):
        for item in self.inside:
            print(item.name)

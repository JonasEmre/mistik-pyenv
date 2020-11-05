from items.items import Items

class Armors(Items):
    def __init__(self, name, value, AC):
        super().__init__(name, value, is_equipable=True, is_collectable=True)
        self.ac = AC

cloth = Armors('Cloth', 0, 7)
leather_armor = Armors('Leather Armor', 24, 15)

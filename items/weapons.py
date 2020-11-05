from items.items import Items

class Weapons(Items):
    def __init__(self, name, value, damage):
        super().__init__(name, value, is_equipable=True, is_collectable=True)
        self.damage = damage

unarmed = Weapons('Unarmed', 25, 4)
short_sword = Weapons('Short Sword', 25, 10)
long_sword = Weapons('Long Sword', 32, 14)

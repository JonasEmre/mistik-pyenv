from items.items import Items
from game_mechanics.dice import Dice, four_sided, six_sided, eight_sided, ten_sided, twenty_sided

class Weapons(Items):
    def __init__(self, name, value):
        super().__init__(name, value, is_equipable=True, is_collectable=True)

    @property
    def dice_type(self):
        if self.name == 'Short Sword':
            return 4
        elif self.name == 'Long Sword':
            return 6
        elif self.name == 'Axe':
            return 6
        elif self.name == 'Bastard Sword':
            return 8
        elif self.name == 'Long Axe':
            return 8

    
    @property
    def damage(self):
        if self.dice_type == 4:
            return four_sided.roll()
        elif self.dice_type == 6:
            return six_sided.roll()
        elif self.dice_type == 8:
            return eight_sided.roll()
        elif self.dice_type == 10:
            return ten_sided.roll()
        elif self.dice_type == 20:
            return twenty_sided.roll()
        
        
    def hit(self):
        pass

unarmed = Weapons('Unarmed', 25)
short_sword = Weapons('Short Sword', 25)
long_sword = Weapons('Long Sword', 32)

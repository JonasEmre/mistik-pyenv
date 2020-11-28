from items.items import Items
from items.weapons import Weapons, unarmed
from items.armors import Armors, cloth
from game_mechanics.inventory import Inventory


class Characters:
    def __init__(self, name, weapon, armor,
                 strength, dexterity, intelligence, location, inventory=Inventory(), gold=0, target=None,
                 is_attacking=False, is_defending=False):
        self.name = name
        self.gold = gold
        self.target = target
        self.location = location
        self.last_location = location
        self.is_attacking = is_attacking
        self.is_defending = is_defending
        if isinstance(weapon, Weapons):
            self.weapon = weapon
        else:
            self.weapon = unarmed
        if isinstance(armor, Armors):
            self.armor = armor
        else:
            self.armor = cloth
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.hp = strength
        self.stamina = dexterity
        self.mana = intelligence
        self.inventory = inventory

    @property
    def max_stamina(self):
        return self.dexterity

    @property
    def max_mana(self):
        return self.intelligence

    @property
    def max_hp(self):
        return self.strength

    @property
    def damage(self):
        if self.is_alive:
            if self.weapon.name == 'unarmed':
                return self.strength * 0.1
            elif isinstance(self.weapon, Weapons):
                return self.weapon.damage + (self.strength * 0.1)

    def equip(self, item_to_equip):
        if self.is_alive:
            for item in self.inventory.inside:
                if item_to_equip == item.name and item.is_equipable == True:
                    if isinstance(item, Weapons):
                        if self.weapon.name is not 'Unarmed':
                            self.inventory.add_item(self.weapon)
                            self.weapon = unarmed
                        self.weapon = item
                    elif isinstance(item, Armors):
                        if self.armor.name is not 'Cloth':
                            self.inventory.add_item(self.armor)
                            self.armor = 'Cloth'
                        self.armor = item
                    self.inventory.rem_item(item_to_equip)

    def unequip(self, target):
        if self.is_alive:
            if self.weapon.name is not 'Unarmed' and isinstance(target, Weapons):
                self.inventory.add_item(self.weapon)
                self.weapon = unarmed
            elif self.armor.name is not 'Cloth' and isinstance(target, Armors):
                self.inventory.add_item(self.armor)
                self.armor = cloth

    def get_item(self, item):
        if self.is_alive:
            if isinstance(item, Items):
                if item.is_collectable:
                    self.inventory.add_item(item)

    def use_item(self, item):
        if self.is_alive:
            if isinstance(item, Items) and item.is_usable == True:
                target_item = self.inventory.find_item(item.name)
                if target_item is not None:
                    target_item.use(self)
                    if item.one_time_use:
                        self.inventory.rem_item(item.name)

    @property
    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False

    def get_dmg(self, damage):
        if self.is_alive:
            self.hp = self.hp - damage

    def __repr__(self):
        return '{}, HP: {}\nWeapon: {}\nArmor: {}'.format(self.name, self.hp, self.weapon.name,
                                                          self.armor.name)

from items import Items
from characters import Characters

class Potions(Items):
    def __init__(self, name, value, effect_type, effect_value):
        super().__init__(name, value, is_collectable=True, is_usable=True, one_time_use=True)
        self.effect_type = effect_type
        self.effect_value = effect_value


    def use(self, user):
        if isinstance(user, Characters):
            if user.is_alive:
                if self.effect_type == 'hp':
                    user.hp += self.effect_value
                    if user.hp > user.max_hp:
                        user.hp = user.max_hp
                elif self.effect_type == 'stamina':
                    user.stamina += self.effect_value
                    if user.stamina > user.max_stamina:
                        user.stamina = user.max_stamina
                elif self.effect_type == 'mana':
                    user.mana += self.effect_value
                    if user.mana > user.max_mana:
                        user.mana = user.max_mana
                return True
            else:
                return False

health_potion= Potions('Health Potion', 3, 'hp', 25)
stamina_potion= Potions('Stamina Potion', 2, 'stamina', 35)
mana_potion= Potions('Mana Potion', 4, 'mana', 20)

        

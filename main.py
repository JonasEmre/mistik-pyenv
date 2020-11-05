from items import Items
from weapons import Weapons, short_sword, long_sword, unarmed
from armors import Armors, leather_armor, cloth
from characters import Characters
from potions import health_potion, stamina, potion, mana_potion


habel = Characters('Habel', weapon=short_sword, armor=leather_armor,
                   strength=100, dexterity=100, intelligence=25)
cain = Characters('Cain', weapon=unarmed, armor=cloth,
                  strength=90, dexterity=90, intelligence=45)
habel.inventory.add_item(long_sword)
print(habel)



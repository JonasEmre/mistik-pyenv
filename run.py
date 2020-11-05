from items.items import Items
from items.weapons import Weapons, short_sword, long_sword, unarmed
from items.armors import Armors, leather_armor, cloth
from chars.characters import Characters
from items.potions import health_potion, stamina_potion, mana_potion


habel = Characters('Habel', weapon=short_sword, armor=leather_armor,
                   strength=100, dexterity=100, intelligence=25)
cain = Characters('Cain', weapon=unarmed, armor=cloth,
                  strength=90, dexterity=90, intelligence=45)
habel.inventory.add_item(long_sword)
habel.get_dmg(50)
habel.inventory.add_item(health_potion)
habel.inventory.check()
print(habel)
print("****************")
habel.use_item(health_potion)
item = habel.inventory.find_item('Health Potion')
print(habel)
habel.inventory.check()

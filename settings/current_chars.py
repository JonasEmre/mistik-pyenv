from items.weapons import Weapons, short_sword, long_sword, unarmed
from items.armors import Armors, leather_armor, cloth
from chars.characters import Characters

habel = Characters('Habel', weapon=short_sword, armor=leather_armor,
                   strength=100, dexterity=100, intelligence=25)
cain = Characters('Cain', weapon=unarmed, armor=cloth,
                  strength=90, dexterity=90, intelligence=45)

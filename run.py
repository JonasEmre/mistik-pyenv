from game_mechanics.game_loop import Application
from settings.current_chars import habel, cain
from world.locations import ancyra


turn = 0
app = Application()

print(habel)
print('***********')
print(cain)
print('***********')
print(ancyra)

for location in ancyra.connections:
    print(ancyra.connections[location])

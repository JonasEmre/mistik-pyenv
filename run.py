from game_mechanics.game_loop import Application
from settings.current_chars import habel, cain
from world.locations import world_locations
from game_mechanics.actions import Action


turn = 0
app = Application()

print(world_locations)
print('*************')
print(habel.location)
Action.move(habel, habel.location, 'Ancyra City Bank')
print('********')
print(habel.location)

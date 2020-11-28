from world.locations import *

ancyra = City(name='Ancyra',
              connections = {'north': 'Crossroad',
                             'east': 'None',
                             'south': 'Steppe',
                             'west': 'None'},
              castle=Castle('Ancyra Castle', Location("Anitta's Hall"), Location('Ancyra Castle Enterance'),
                            Location('Ancyra Castle Dungeon')),
              bank=Bank('Ancyra City Bank'),
              temple=Temple('Temple'),
              market=Market('Market'),
              city_hall=CityHall('Ancyra City Hall'),
              holdings={'main': Guild('Red Guild'), 'secondary': Guild('Blue Guild')})

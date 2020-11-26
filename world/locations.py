class World:
    world_locations = []
    def __init__(self):
        pass
        
class Location(World):
    def __init__(self, name, connections=dict()):
        super().__init__()
        self.name = name
        self.connections = connections


    def __repr__(self):
        return '{}'.format(self.name)


class City(Location):
    def __init__(self, name, connections, castle, bank, temple, market, city_hall,
                 holdings={'main': None, 'secondary': None}):
        super().__init__(name, connections)
        self.castle = castle
        self.bank = bank
        self.temple = temple
        self.market = market
        self.city_hall = city_hall
        self.holdings = holdings


class Castle(Location):
    def __init__(self, name):
        super().__init__(name)


class Bank(Location):
    def __init__(self, name):
        super().__init__(name)


class Temple(Location):
    def __init__(self, name):
        super().__init__(name)


class Market(Location):
    def __init__(self, name):
        super().__init__(name)


class CityHall(Location):
    def __init__(self, name):
        super().__init__(name)


class Guild(Location):
    def __init__(self, name):
        super().__init__(name)



ancyra = City(name='Ancyra',
              connections = {'north': 'Crossroad',
                             'east': 'None',
                             'south': 'Steppe',
                             'west': 'None'},
              castle=Castle("Lord's Castle"),
              bank=Bank('City Bank'),
              temple=Temple('Temple'),
              market=Market('Market'),
              city_hall=CityHall('City Hall'),
              holdings={'main': Guild('Red Guild'), 'secondary': Guild('Blue Guild')})

crossroad = Location('Crossroad',
                     connections = {'north': 'Dungeon',
                             'east': 'East',
                             'south': 'Ancyra',
                             'west': 'Graveyard'})

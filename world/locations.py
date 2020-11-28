world_locations = []
class World:
    def __init__(self):
        world_locations.append(self)
        
class Location(World):
    def __init__(self, name, connections=dict(), places=[], back=None):
        super().__init__()
        self.name = name
        self.connections = connections
        self.places = places
        self.back = back

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
        self.places.extend([self.castle, self.bank, self.temple, self.market, self.city_hall])
        


class Castle(Location):
    def __init__(self, name, lords_hall, enterance, dungeon):
        super().__init__(name)
        self.lords_hall = lords_hall
        self.enterance = enterance
        self.dungeon = dungeon


class Bank(Location):
    def __init__(self, name):
        super().__init__(name)
        self.chest = {'Amount': 0, 'Rate': float(3)}
        self.clerk = {'Debt': 0, 'Interest': float(4)}


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

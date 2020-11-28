from chars.characters import Characters
from world.locations import Location, world_locations


class Action():
    def __init__(self, owner, oppenent):
        self.owner = owner
        self.opponent = opponent


    def execute(self):
        pass


    @staticmethod
    def move(subject, location, target):
        if isinstance(subject, Characters) and isinstance(location, Location) and subject.is_alive==True:
            #print('Debug Move')
            old_location = subject.location
            new_location = None
            for location in world_locations:
                if target == location.name:
                    new_location = location
                    #print('{}'.format(new_location))
                    subject.location = new_location
            
            

class Attack(Action):
    def __init__(self, owner, opponent):
        super().__init__(owner, opponent)

    def execute(self):
        if isinstance(self.owner, Characters) and isinstance(self.opponent, Characters):
            self.owner.is_attacking = True
            self.opponent.is_defending = True
            self.owner.target = self.opponent
            self.opponent.target = self.owner
            self.opponent.get_dmg(self.owner.damage)

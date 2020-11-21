from chars.characters import Characters

class Actions():
    def __init__(self, owner, opponent):
        self.owner = owner
        self.opponet = opponet


    def execute(self):
        pass


class Attack(Actions):
    def __init__(self, owner, opponet):
        super().__init__(owner, opponet)

        
    def execute(self):
        if isinstance(self.owner, Characters) and isinstance(self.opponet, Characters):
            self.owner.is_attacking = True
            self.opponet.is_defending = True
            self.owner.target = self.opponet
            self.opponet.target = self.owner
            self.opponet.get_dmg(self.owner.damage)
            
        
            
            

        
        

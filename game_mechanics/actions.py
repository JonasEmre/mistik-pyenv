from chars.characters import Characters


class Actions():
    def __init__(self, owner, opponent):
        self.owner = owner
        self.opponent = opponent

    def execute(self):
        pass


class Attack(Actions):
    def __init__(self, owner, opponent):
        super().__init__(owner, opponent)

    def execute(self):
        if isinstance(self.owner, Characters) and isinstance(self.opponent, Characters):
            self.owner.is_attacking = True
            self.opponent.is_defending = True
            self.owner.target = self.opponent
            self.opponent.target = self.owner
            self.opponent.get_dmg(self.owner.damage)

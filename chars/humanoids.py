from chars.characters import Characters


class Humanoids(Characters):

    def __init__(self, name, weapon='unarmed', armor='cloth'):
        super().__init__(name, weapon, armor)

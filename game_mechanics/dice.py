import random


class Dice:
    def __init__(self, lowest, highest, bless=0):
        self.lowest = lowest
        self.highest = highest
        self.bless = bless

    def roll(self):
        return random.randint(self.lowest, self.highest) + self.bless


four_sided = Dice(1, 4)
six_sided = Dice(1, 6)
eight_sided = Dice(1, 8)
ten_sided = Dice(1, 10)
twenty_sided = Dice(1, 20)

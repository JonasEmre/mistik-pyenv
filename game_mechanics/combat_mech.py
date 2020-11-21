from chars.characters import Characters


class Combat():

    @staticmethod
    def battle(attacker, defender):
        if isinstance(attacker, Characters) and isinstance(defender, Characters):
            if attacker.is_alive is True and defender.is_alive is True:
                attacker.target = defender
                defender.target = attacker

from chars.characters import Characters


class Application():
    def __init__(self, is_active=True, global_turn=0):
        self.name = 'Mistik-Pyenv'
        self.is_active = is_active
        self.global_turn = global_turn
        
class Loop():
    def __init__(self, local=0, general=0):
        self.local = local
        self.general = general
        

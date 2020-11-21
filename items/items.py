class Items:
    def __init__(self, name, value, is_equipable, is_collectable, is_usable=False, one_time_use=False):
        self.name = name
        self.value = value
        self.is_equipable = is_equipable
        self.is_collectable = is_collectable
        self.is_usable = is_usable
        self.one_time_use = one_time_use

    def __repr__(self):
        return '{}, Value: {}'.format(self.name, self.value)

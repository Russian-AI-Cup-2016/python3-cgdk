from model.World import World


class PlayerContext:
    def __init__(self, wizards, world: (None, World)):
        self.wizards = wizards
        self.world = world

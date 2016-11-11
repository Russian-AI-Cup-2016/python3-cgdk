class World:
    def __init__(self, tick_index, tick_count, width, height, players, wizards, minions, projectiles, bonuses,
                 buildings, trees):
        self.tick_index = tick_index
        self.tick_count = tick_count
        self.width = width
        self.height = height
        self.players = players
        self.wizards = wizards
        self.minions = minions
        self.projectiles = projectiles
        self.bonuses = bonuses
        self.buildings = buildings
        self.trees = trees

    def get_my_player(self):
        for player in self.players:
            if player.me:
                return player

        return None

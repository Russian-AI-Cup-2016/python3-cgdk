from model.Faction import Faction


class Player:
    def __init__(self, id, me, name, strategy_crashed, score, faction: (None, Faction)):
        self.id = id
        self.me = me
        self.name = name
        self.strategy_crashed = strategy_crashed
        self.score = score
        self.faction = faction

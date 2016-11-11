from model.Faction import Faction
from model.LivingUnit import LivingUnit


class Tree(LivingUnit):
    def __init__(self, id, x, y, speed_x, speed_y, angle, faction: (None, Faction), radius, life, max_life, statuses):
        LivingUnit.__init__(self, id, x, y, speed_x, speed_y, angle, faction, radius, life, max_life, statuses)

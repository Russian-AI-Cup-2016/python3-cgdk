from model.CircularUnit import CircularUnit
from model.Faction import Faction


class LivingUnit(CircularUnit):
    def __init__(self, id, x, y, speed_x, speed_y, angle, faction: (None, Faction), radius, life, max_life, statuses):
        CircularUnit.__init__(self, id, x, y, speed_x, speed_y, angle, faction, radius)

        self.life = life
        self.max_life = max_life
        self.statuses = statuses

from model.BonusType import BonusType
from model.CircularUnit import CircularUnit
from model.Faction import Faction


class Bonus(CircularUnit):
    def __init__(self, id, x, y, speed_x, speed_y, angle, faction: (None, Faction), radius, type: (None, BonusType)):
        CircularUnit.__init__(self, id, x, y, speed_x, speed_y, angle, faction, radius)

        self.type = type

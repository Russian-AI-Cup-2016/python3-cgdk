from math import *

from model.Faction import Faction


class Unit:
    def __init__(self, id, x, y, speed_x, speed_y, angle, faction: (None, Faction)):
        self.id = id
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.angle = angle
        self.faction = faction

    def get_angle_to(self, x, y):
        absolute_angle_to = atan2(y - self.y, x - self.x)
        relative_angle_to = absolute_angle_to - self.angle

        while relative_angle_to > pi:
            relative_angle_to -= 2.0 * pi

        while relative_angle_to < -pi:
            relative_angle_to += 2.0 * pi

        return relative_angle_to

    def get_angle_to_unit(self, unit):
        return self.get_angle_to(unit.x, unit.y)

    def get_distance_to(self, x, y):
        return hypot(x - self.x, y - self.y)

    def get_distance_to_unit(self, unit):
        return self.get_distance_to(unit.x, unit.y)

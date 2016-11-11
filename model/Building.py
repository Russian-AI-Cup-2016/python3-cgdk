from model.BuildingType import BuildingType
from model.Faction import Faction
from model.LivingUnit import LivingUnit


class Building(LivingUnit):
    def __init__(self, id, x, y, speed_x, speed_y, angle, faction: (None, Faction), radius, life, max_life, statuses,
                 type: (None, BuildingType), vision_range, attack_range, damage, cooldown_ticks,
                 remaining_action_cooldown_ticks):
        LivingUnit.__init__(self, id, x, y, speed_x, speed_y, angle, faction, radius, life, max_life, statuses)

        self.type = type
        self.vision_range = vision_range
        self.attack_range = attack_range
        self.damage = damage
        self.cooldown_ticks = cooldown_ticks
        self.remaining_action_cooldown_ticks = remaining_action_cooldown_ticks

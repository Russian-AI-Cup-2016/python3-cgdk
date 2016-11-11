from model.CircularUnit import CircularUnit
from model.Faction import Faction
from model.ProjectileType import ProjectileType


class Projectile(CircularUnit):
    def __init__(self, id, x, y, speed_x, speed_y, angle, faction: (None, Faction), radius,
                 type: (None, ProjectileType), owner_unit_id, owner_player_id):
        CircularUnit.__init__(self, id, x, y, speed_x, speed_y, angle, faction, radius)

        self.type = type
        self.owner_unit_id = owner_unit_id
        self.owner_player_id = owner_player_id

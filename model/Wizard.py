from model.Faction import Faction
from model.LivingUnit import LivingUnit


class Wizard(LivingUnit):
    def __init__(self, id, x, y, speed_x, speed_y, angle, faction: (None, Faction), radius, life, max_life, statuses,
                 owner_player_id, me, mana, max_mana, vision_range, cast_range, xp, level, skills,
                 remaining_action_cooldown_ticks, remaining_cooldown_ticks_by_action, master, messages):
        LivingUnit.__init__(self, id, x, y, speed_x, speed_y, angle, faction, radius, life, max_life, statuses)

        self.owner_player_id = owner_player_id
        self.me = me
        self.mana = mana
        self.max_mana = max_mana
        self.vision_range = vision_range
        self.cast_range = cast_range
        self.xp = xp
        self.level = level
        self.skills = skills
        self.remaining_action_cooldown_ticks = remaining_action_cooldown_ticks
        self.remaining_cooldown_ticks_by_action = remaining_cooldown_ticks_by_action
        self.master = master
        self.messages = messages

from model.LaneType import LaneType
from model.SkillType import SkillType


class Message:
    def __init__(self, lane: (None, LaneType), skill_to_learn: (None, SkillType), raw_message):
        self.lane = lane
        self.skill_to_learn = skill_to_learn
        self.raw_message = raw_message

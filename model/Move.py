class Move:
    def __init__(self):
        self.speed = 0.0
        self.strafe_speed = 0.0
        self.turn = 0.0
        self.action = None
        self.cast_angle = 0.0
        self.min_cast_distance = 0.0
        self.max_cast_distance = 10000.0
        self.status_target_id = -1
        self.skill_to_learn = None
        self.messages = None

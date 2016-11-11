from model.StatusType import StatusType


class Status:
    def __init__(self, id, type: (None, StatusType), wizard_id, player_id, remaining_duration_ticks):
        self.id = id
        self.type = type
        self.wizard_id = wizard_id
        self.player_id = player_id
        self.remaining_duration_ticks = remaining_duration_ticks

from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    INIT_OXY_LEVEL = float(540)

    def __init__(self, name: str):
        super().__init__(name, ScubaDiver.INIT_OXY_LEVEL)

    def miss(self, time_to_catch: int):
        if self.oxygen_level - time_to_catch < 0:
            self.oxygen_level = 0

        else:
            self.oxygen_level -= int(time_to_catch * 0.3)

    def renew_oxy(self):

        self.oxygen_level = ScubaDiver.INIT_OXY_LEVEL

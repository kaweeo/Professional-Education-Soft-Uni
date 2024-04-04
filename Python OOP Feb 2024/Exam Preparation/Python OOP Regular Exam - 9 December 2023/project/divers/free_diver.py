from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    INIT_OXY_LEVEL = float(120)

    def __init__(self, name: str):
        super().__init__(name, self.INIT_OXY_LEVEL)

    def miss(self, time_to_catch: int):
        if self.oxygen_level - time_to_catch < 0:
            self.oxygen_level = 0

        else:
            self.oxygen_level -= round(time_to_catch * 0.6)

    def renew_oxy(self):

        self.oxygen_level = FreeDiver.INIT_OXY_LEVEL

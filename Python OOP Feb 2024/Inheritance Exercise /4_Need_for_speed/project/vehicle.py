class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: float = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
        self.fuel = fuel
        self.horse_power = horse_power

    def drive(self, kilometers: int):
        needed_fuel = self.fuel_consumption * kilometers
        if self.fuel >= needed_fuel:
            self.fuel -= needed_fuel

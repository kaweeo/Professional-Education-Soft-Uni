from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        ...

    @abstractmethod
    def refuel(self, fuel):
        ...


class Car(Vehicle):
    SUMMER_CONSUMPTION = 0.9

    def drive(self, distance):
        consumption = (self.fuel_consumption + self.SUMMER_CONSUMPTION) * distance
        if not consumption > self.fuel_quantity:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    SUMMER_CONSUMPTION = 1.6
    TRUCKS_LEAK = 0.95

    def drive(self, distance):
        consumption = (self.fuel_consumption + self.SUMMER_CONSUMPTION) * distance
        if not consumption > self.fuel_quantity:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.TRUCKS_LEAK


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

# SOLUTION 2

# from abc import ABC, abstractmethod
#
#
# class Vehicle(ABC):  # Abstract Base Class
#     def __init__(self, fuel_quantity: float, fuel_consumption: float):
#         self.fuel_quantity = fuel_quantity
#         self.fuel_consumption = fuel_consumption
#
#     @property
#     @abstractmethod
#     def conditioner_on(self) -> float:
#         ...
#
#     def drive(self, distance: float) -> None:
#         consumption = (self.conditioner_on + self.fuel_consumption) * distance
#
#         if self.fuel_quantity >= consumption:
#             self.fuel_quantity -= consumption
#
#     @abstractmethod
#     def refuel(self, fuel: float) -> None:
#         pass
#
#
# class Car(Vehicle):
#
#     @property
#     def conditioner_on(self) -> float:
#         return 0.9
#
#     def refuel(self, fuel: float) -> None:
#         self.fuel_quantity += fuel
#
#
# class Truck(Vehicle):
#     TANK_PERCENTAGE_FILL: float = 0.95
#
#     @property
#     def conditioner_on(self) -> float:
#         return 1.6
#
#     def refuel(self, fuel: float) -> None:
#         self.fuel_quantity += fuel * self.TANK_PERCENTAGE_FILL

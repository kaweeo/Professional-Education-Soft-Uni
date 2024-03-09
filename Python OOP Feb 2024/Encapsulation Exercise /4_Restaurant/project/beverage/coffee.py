from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name: str, caffeine: float):
        super().__init__(name, Coffee.PRICE, Coffee.MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine

# from project.beverage.hot_beverage import HotBeverage
#
#
# class Coffee(HotBeverage):
#     MILLILITERS = 50
#     PRICE = 3.50
#
#     def __init__(self, name: str, price: float, milliliters: float, caffeine: float):
#         super().__init__(name, price, milliliters)
#         self.__caffeine = caffeine
#         self.MILLILITERS = Coffee.MILLILITERS
#         self.PRICE = Coffee.PRICE
#
#     @property
#     def caffeine(self):
#         return self.__caffeine

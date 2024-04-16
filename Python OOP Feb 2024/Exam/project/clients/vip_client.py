from math import floor

from project.clients.base_client import BaseClient


class VIPClient(BaseClient):
    MEMBERSHIP_TYPE = "VIP"

    def __init__(self, name: str):
        super().__init__(name, self.MEMBERSHIP_TYPE)

    def earning_points(self, order_amount: float):
        earned_points = floor(order_amount / 5)
        self.points += earned_points

        return earned_points



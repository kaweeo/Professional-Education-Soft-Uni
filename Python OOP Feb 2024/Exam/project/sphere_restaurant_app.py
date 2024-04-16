from typing import List

from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    VALID_WAITERS = {
        "FullTimeWaiter": FullTimeWaiter,
        "HalfTimeWaiter": HalfTimeWaiter,
    }

    VALID_CLIENTS = {
        "RegularClient": RegularClient,
        "VIPClient": VIPClient,
    }

    def __init__(self):
        self.waiters: List[FullTimeWaiter, HalfTimeWaiter] = []
        self.clients: List[RegularClient, VIPClient] = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in self.VALID_WAITERS.keys():
            return f"{waiter_type} is not a recognized waiter type."

        waiter = next(filter(lambda w: w.name == waiter_name, self.waiters), None)
        if waiter:
            return f"{waiter_name} is already on the staff."

        waiter = self.VALID_WAITERS[waiter_type](waiter_name, hours_worked)
        self.waiters.append(waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        if client_type not in self.VALID_CLIENTS.keys():
            return f"{client_type} is not a recognized client type."

        client = next(filter(lambda c: c.name == client_name, self.clients), None)
        if client:
            return f"{client_name} is already a client."

        client = self.VALID_CLIENTS[client_type](client_name)
        self.clients.append(client)
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        waiter = next(filter(lambda w: w.name == waiter_name, self.waiters), None)
        if not waiter:
            return f"No waiter found with the name {waiter_name}."

        return waiter.report_shift()  # TODO: CARE HERE

    def process_client_order(self, client_name: str, order_amount: float):
        client = next(filter(lambda c: c.name == client_name, self.clients), None)
        if not client:
            return f"{client_name} is not a registered client."

        points_earned = client.earning_points(order_amount)
        return f"{client_name} earned {points_earned} points from the order."

    def apply_discount_to_client(self, client_name: str):
        client = next(filter(lambda c: c.name == client_name, self.clients), None)
        if not client:
            return f"{client_name} cannot get a discount because this client is not admitted!"

        discount_percentage, remaining_points = client.apply_discount()
        return f"{client_name} received a {discount_percentage}% discount. Remaining points {remaining_points}"

    def generate_report(self):

        total_earnings = 0
        for waiter in self.waiters:
            waiter_earnings = waiter.calculate_earnings()
            total_earnings += waiter_earnings

        total_client_points = 0
        for client in self.clients:
            total_client_points += client.points

        result = f"$$ Monthly Report $$\nTotal Earnings: ${total_earnings:.2f}\n" \
                 f"Total Clients Unused Points: {total_client_points}\nTotal Clients Count: {len(self.clients)}\n** Waiter Details **"

        sorted_waiters = sorted(self.waiters, key=lambda w: w.calculate_earnings(), reverse=True)

        waiter_details_result = ""

        for waiter in sorted_waiters:
            waiter_details_result += f"\nName: {waiter.name}, Total earnings: ${waiter.calculate_earnings():.2f}"

        return result + waiter_details_result



































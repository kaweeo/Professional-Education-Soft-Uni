from copy import deepcopy
from typing import List

from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.starter import Starter
from project.client import Client


class FoodOrdersApp:
    VALID_MEALS = ["Starter", "MainDish", "Dessert"]
    receipt_id = 0

    def __init__(self):
        self.menu: List[MainDish, Dessert, Starter] = []
        self.clients_list: List[Client] = []

    def register_client(self, client_phone_number: str):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list), None)
        if client:
            raise Exception("The client has already been registered!")

        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if meal.__class__.__name__ in self.VALID_MEALS:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        # for meal in self.menu:
        #     meal.details()

        result = [meal.details() for meal in self.menu]

        return '\n'.join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self.shopping_cart_names = []
        self.shopping_cart_total = 0

        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list), None)
        if not client:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        for meal_name in meal_names_and_quantities.keys():
            if meal_name not in [meal.name for meal in self.menu]:
                raise Exception(f"{meal_name} is not on the menu!")  # TODO: CARE HERE

        for meal_name, quantity in meal_names_and_quantities.items():
            meal = next(filter(lambda m: m.name == meal_name, self.menu))
            if meal.quantity < quantity:
                raise Exception(f"Not enough quantity of {type(meal.__class__)}: {meal_name}!")

        shopping_cart_names = []
        shopping_cart_total = 0

        for meal_name, quantity in meal_names_and_quantities.items():
            meal = next(filter(lambda m: m.name == meal_name, self.menu))

            ordered_meal = deepcopy(meal)
            ordered_meal.quantity = quantity

            client.shopping_cart.append(ordered_meal)
            shopping_cart_names.append(meal_name)
            client.bill += meal.price * quantity
            meal.quantity -= quantity
            shopping_cart_total += meal.price * quantity

        return f"Client {client_phone_number} successfully ordered {', '.join(shopping_cart_names)} for {shopping_cart_total:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        for ordered_meal in client.shopping_cart:
            for meal in self.menu:
                if ordered_meal == meal:
                    meal.quantity += ordered_meal.quantity

        client.shopping_cart = []
        client.bill = 0.0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        client.shopping_cart = []
        total_paid_money = client.bill
        client.bill = 0.0
        self.receipt_id += 1

        return f"Receipt #{self.receipt_id} with total amount of {total_paid_money:.2f}" \
               f" was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

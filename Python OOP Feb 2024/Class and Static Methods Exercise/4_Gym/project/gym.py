from typing import List

from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:

    def __init__(self) -> None:
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer) -> None:
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer) -> None:
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment) -> None:
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan) -> None:
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription) -> None:
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int) -> str:
        searched_objts = []

        searched_subscription = next(filter(lambda s: s.id == subscription_id, self.subscriptions))
        searched_objts.append(searched_subscription)

        searched_customer_id = searched_subscription.customer_id
        searched_customer = next(filter(lambda c: c.id == searched_customer_id, self.customers))
        searched_objts.append(searched_customer)

        searched_trainer_id = searched_subscription.trainer_id
        searched_trainer = next(filter(lambda t: t.id == searched_trainer_id, self.trainers))
        searched_objts.append(searched_trainer)

        searched_equipment = next(filter(lambda e: e.id == subscription_id, self.equipment))
        searched_objts.append(searched_equipment)

        searched_plan = next(filter(lambda p: p.id == subscription_id, self.plans))
        searched_objts.append(searched_plan)

        return "\n".join(str(e) for e in searched_objts)

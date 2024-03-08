from typing import List

from project.animal import Animal
from project.keeper import Keeper
from project.caretaker import Caretaker
from project.vet import Vet
from project.lion import Lion
from project.tiger import Tiger
from project.cheetah import Cheetah
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List = []
        self.workers: List = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if price <= self.__budget and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if price <= self.__budget and not self.__animal_capacity < len(self.animals):
            return "Not enough space for animal"

        if price > self.__budget:
            return "Not enough budget"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        try:
            searched_worker = next(filter(lambda w: worker_name == w.name, self.workers))
            self.workers.remove(searched_worker)
            return f"{worker_name} fired successfully"
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        sum_of_workers_salaries = sum([w.salary for w in self.workers])
        if self.__budget >= sum_of_workers_salaries:
            self.__budget -= sum_of_workers_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        sum_tend_of_animals = sum([animal.money_for_care for animal in self.animals])
        if self.__budget >= sum_tend_of_animals:
            self.__budget -= sum_tend_of_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount) -> None:
        self.__budget += amount

    def animals_status(self) -> str:

        lions = [l for l in self.animals if l.__class__.__name__ == "Lion"]
        tigers = [t for t in self.animals if t.__class__.__name__ == "Tiger"]
        cheetahs = [c for c in self.animals if c.__class__.__name__ == "Cheetah"]

        result = f"You have {len(self.animals)} animals"
        result += f"\n----- {len(lions)} Lions:\n"
        result += "\n".join(l.__repr__() for l in lions)
        result += f"\n----- {len(tigers)} Tigers:\n"
        result += "\n".join(t.__repr__() for t in tigers)
        result += f"\n----- {len(cheetahs)} Cheetahs:\n"
        result += "\n".join(c.__repr__() for c in cheetahs)
        return result

    def workers_status(self) -> str:
        result = ""

        keepers = [k for k in self.workers if k.__class__.__name__ == "Keeper"]
        caretakers = [c for c in self.workers if c.__class__.__name__ == "Caretaker"]
        vets = [v for v in self.workers if v.__class__.__name__ == "Vet"]

        result += f"You have {len(self.workers)} workers"
        result += f"\n----- {len(keepers)} Keepers:\n"
        result += "\n".join(k.__repr__() for k in keepers)
        result += f"\n----- {len(caretakers)} Caretakers:\n"
        result += "\n".join(c.__repr__() for c in caretakers)
        result += f"\n----- {len(vets)} Vets:\n"
        result += "\n".join(v.__repr__() for v in vets)
        return result

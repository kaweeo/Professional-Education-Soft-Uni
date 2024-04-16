from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, capacity=30)
        self.robots: List[FemaleRobot[BaseRobot], MaleRobot[BaseRobot]] = []

    def details(self):
        robots_names = [r.name for r in self.robots]
        if not self.robots:
            result = f"{self.name} Main Service:\n" \
                     f"Robots: none"
            return result

        result = f"{self.name} Main Service:\n" \
                 f"Robots: {' '.join(robots_names)}"
        return result

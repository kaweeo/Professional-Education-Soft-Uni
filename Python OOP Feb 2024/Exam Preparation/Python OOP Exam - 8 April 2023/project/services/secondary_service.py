from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name: str, capacity: int = 15):
        super().__init__(name, capacity)

    def details(self):
        robots_names = [r.name for r in self.robots]
        if not robots_names:
            robots_names = "none"

        result = f"{self.name} Secondary Service:\n" \
                 f"Robots: {' '.join(robots_names)}"  # care space
        return result

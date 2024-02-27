
class Hero:
    def __init__(self, name: str, health: int or float):
        self.name = name
        self.health = health

    def defend(self, damage: int or float):
        if damage >= self.health:
            self.health = 0
            return f"{self.name} was defeated"

        self.health -= damage

    def heal(self, amount: int or float):
        self.health += amount

hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))

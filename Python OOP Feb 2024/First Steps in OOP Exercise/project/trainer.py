from project.pokemon import Pokemon

class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"

        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        try:
            filter_obj = next(filter(lambda p: pokemon_name == p.name, self.pokemons))
            self.pokemons.remove(filter_obj)
            return f"You have released {pokemon_name}"

        except StopIteration:
            return "Pokemon is not caught"

    def trainer_data(self):
        return f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n" + \
            "\n".join([f"- {p.pokemon_details()}" for p in self.pokemons])

pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
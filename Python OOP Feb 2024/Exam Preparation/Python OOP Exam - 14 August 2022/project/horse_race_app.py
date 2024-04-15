from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    HORSES_MAPPER = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred,
    }
    VALID_TYPE_RACES = ["Winter", "Spring", "Autumn", "Summer"]

    def __init__(self):
        self.horses: List[Appaloosa: Horse, Thoroughbred: Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        searched_horse = next(filter(lambda h: h.name == horse_name, self.horses), None)
        if searched_horse:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.HORSES_MAPPER.keys():
            new_horse = self.HORSES_MAPPER[horse_type](horse_name, horse_speed)
            self.horses.append(new_horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        searched_jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys), None)
        if searched_jockey:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jocker = Jockey(jockey_name, age)
        self.jockeys.append(new_jocker)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        for race in self.horse_races:
            if race.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")

        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        try:
            jokey = next(filter(lambda j: j.name == jockey_name, self.jockeys))
        except IndexError:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        horses_list_of_the_needed_type = [h for h in self.horses if h.__class__.__name__ == horse_type]
        if not horses_list_of_the_needed_type:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jokey.horse:
            return f"Jockey {jockey_name} already has a horse."

        for horse in horses_list_of_the_needed_type[::-1]:
            if not horse.is_taken:
                jokey.horse = horse
                horse.is_taken = True
                return f"Jockey {jockey_name} will ride the horse {horse.name}."

        return f"Horse breed {horse_type} could not be found!"

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys), None)

        searched_race = next(filter(lambda r: r.race_type == race_type, self.horse_races), None)
        if not searched_race:
            raise Exception(f"Race {race_type} could not be found!")

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        for horse_race in self.horse_races:
            if horse_race.race_type == race_type:
                if jockey in horse_race.jockeys:
                    return f"Jockey {jockey_name} has been already added to the {race_type} race."
                else:
                    horse_race.jockeys.append(jockey)
                    return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        horse_race = next(filter(lambda r: r.race_type == race_type, self.horse_races), None)
        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winners_speed = 0
        the_winner = None
        for jockey in horse_race.jockeys:
            if jockey.horse.speed > winners_speed:
                the_winner = jockey
                winners_speed = jockey.horse.speed

        return f"The winner of the {race_type} race, with a speed of {winners_speed}km/h is {the_winner.name}!" \
               f" Winner's horse: {the_winner.horse.name}."

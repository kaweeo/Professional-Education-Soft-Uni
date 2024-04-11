from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIANS = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer,
    }

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ConcertTrackerApp.VALID_MUSICIANS.keys():
            raise ValueError("Invalid musician type!")

        musician = next(filter(lambda m: m.name == name, self.musicians), None)
        if musician:
            raise Exception(f"{name} is already a musician!")

        musician = ConcertTrackerApp.VALID_MUSICIANS[musician_type](name, age)
        self.musicians.append(musician)
        return f"{musician.name} is now a {musician_type}."

    def create_band(self, name: str):
        band = next(filter(lambda b: b.name == name, self.bands), None)
        if band:
            raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = next(filter(lambda c: c.place == place, self.concerts), None)
        if concert:
            raise Exception(f"{place} is already registered for {concert.genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = next(filter(lambda m: m.name == musician_name, self.musicians), None)
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        band = next(filter(lambda b: b.name == band_name, self.bands), None)
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = next(filter(lambda b: b.name == band_name, self.bands), None)
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        musician = next(filter(lambda m: m.name == musician_name, band.members), None)
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):

        concert = next(filter(lambda c: c.place == concert_place, self.concerts))
        band = next(filter(lambda b: b.name == band_name, self.bands))

        if len(set(band.members)) < 3:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        band_drummers_list = [memb for memb in band.members if memb.__class__.__name__ == "Drummer"]
        band_guitarist_list = [memb for memb in band.members if memb.__class__.__name__ == "Guitarist"]
        band_singer_list = [memb for memb in band.members if memb.__class__.__name__ == "Singer"]

        playing = True
        if concert.genre == "Rock":
            for drummer in band_drummers_list:
                if "play the drums with drumsticks" not in drummer.skills:
                    playing = False

            for singer in band_singer_list:
                if "sing high pitch notes" not in singer.skills:
                    playing = False

            for guitarist in band_guitarist_list:
                if "play rock" not in guitarist.skills:
                    playing = False

        elif concert.genre == "Metal":
            for drummer in band_drummers_list:
                if "play the drums with drumsticks" not in drummer.skills:
                    playing = False

            for singer in band_singer_list:
                if "sing low pitch notes" not in singer.skills:
                    playing = False

            for guitarist in band_guitarist_list:
                if "play metal" not in guitarist.skills:
                    playing = False

        elif concert.genre == "Jazz":
            for drummer in band_drummers_list:
                if "play the drums with drum brushes" not in drummer.skills:
                    playing = False

            for singer in band_singer_list:
                if "sing low pitch notes" not in singer.skills or "sing high pitch notes" not in singer.skills:
                    playing = False

            for guitarist in band_guitarist_list:
                if "play jazz" not in guitarist.skills:
                    playing = False

        if not playing:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_DIVERS = {
        "FreeDiver": FreeDiver,
        "ScubaDiver": ScubaDiver
    }
    VALID_FISH = {
        "PredatoryFish": PredatoryFish,
        "DeepSeaFish": DeepSeaFish,
    }

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.VALID_DIVERS.keys():
            return f"{diver_type} is not allowed in our competition."

        searched_diver = next(filter(lambda d: d.name == diver_name, self.divers), None)

        if searched_diver:
            return f"{diver_name} is already a participant."

        new_diver = self.VALID_DIVERS[diver_type](diver_name)
        self.divers.append(new_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISH.keys():
            return f"{fish_type} is forbidden for chasing in our competition."

        searched_fish = next(filter(lambda f: f.name == fish_name, self.fish_list), None)
        if searched_fish:
            return f"{fish_name} is already permitted."

        new_fish = self.VALID_FISH[fish_type](fish_name, points)
        self.fish_list.append(new_fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        searched_diver = next(filter(lambda d: d.name == diver_name, self.divers), None)
        if not searched_diver:
            return f"{diver_name} is not registered for the competition."

        searched_fish = next(filter(lambda f: f.name == fish_name, self.fish_list), None)
        if not searched_fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if searched_diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        # TODO CARE
        if searched_diver.oxygen_level < searched_fish.time_to_catch:
            searched_diver.miss(searched_fish.time_to_catch)

            if searched_diver.oxygen_level == 0:
                searched_diver.has_health_issue = True

            return f"{diver_name} missed a good {fish_name}."

        elif searched_diver.oxygen_level == searched_fish.time_to_catch:
            if is_lucky:
                searched_diver.hit(searched_fish)

                if searched_diver.oxygen_level == 0:
                    searched_diver.has_health_issue = True

                return f"{diver_name} hits a {searched_fish.points}pt. {fish_name}."
            else:
                searched_diver.miss(searched_fish.time_to_catch)

                if searched_diver.oxygen_level == 0:
                    searched_diver.has_health_issue = True
                return f"{diver_name} missed a good {fish_name}."

        elif searched_diver.oxygen_level > searched_fish.time_to_catch:
            searched_diver.hit(searched_fish)

            if searched_diver.oxygen_level == 0:
                searched_diver.has_health_issue = True
            return f"{diver_name} hits a {searched_fish.points}pt. {fish_name}."


    def health_recovery(self):
        divers_to_be_health = [d for d in self.divers if d.has_health_issue]
        [d.renew_oxy() for d in divers_to_be_health]
        [d.update_health_status() for d in divers_to_be_health]
        return f"Divers recovered: {len(divers_to_be_health)}"

    def diver_catch_report(self, diver_name: str):
        searched_diver = next(filter(lambda d: d.name == diver_name, self.divers))
        result = f"**{diver_name} Catch Report**\n"
        fish_details = "\n".join(fish.fish_details() for fish in searched_diver.catch)
        result += fish_details
        return result

    def competition_statistics(self):
        good_health_condition_divers = [diver for diver in self.divers if not diver.has_health_issue]
        sorted_good_health_divers = sorted(
            good_health_condition_divers,
            key=lambda d: (-d.competition_points, -len(d.catch), d.name)
        )

        result = "**Nautical Catch Challenge Statistics**\n"
        result += "\n".join(str(d) for d in sorted_good_health_divers)
        return result

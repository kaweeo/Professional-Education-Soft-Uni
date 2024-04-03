
from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp():
    VALID_TYPE_CLIMBERS = {
        "ArcticClimber": ArcticClimber,
        "SummitClimber": SummitClimber
    }

    VALID_TYPE_PEAKS = {
        "ArcticPeak": ArcticPeak,
        "SummitPeak": SummitPeak
    }

    def __init__(self):
        self.climbers = []  # List to store all climber objects registered
        self.peaks = []  # List to store all peak objects that are part of the wish list

    # def register_climber(self, climber_type: str, climber_name: str):
    #     # Check if climber_type is valid
    #     if climber_type not in self.VALID_TYPE_CLIMBERS.keys():
    #         raise KeyError(f"{climber_type} doesn't exist in our register.")
    #
    #         # Check if the climber with the given name already exists
    #     for climber in self.climbers:
    #         if climber.name == climber_name:
    #             return f"{climber_name} has already been registered."
    #
    #     # Create a new climber object and add it to the list of climbers
    #     new_climber = self.VALID_TYPE_CLIMBERS[climber_type](climber_name)
    #     self.climbers.append(new_climber)
    #     return f"{climber_name} has been registered successfully."

    def register_climber(self, climber_type: str, climber_name: str) -> str:
        try:
            climber = self.VALID_TYPE_CLIMBERS[climber_type](climber_name)
        except KeyError:
            return f"{climber_type} doesn't exist in our register."

        try:
            next(filter(lambda c: c.name == climber_name, self.climbers))
            return f"{climber_name} has been already registered."
        except StopIteration:
            self.climbers.append(climber)
            return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.VALID_TYPE_PEAKS.keys():
            return f"{peak_type} is an unknown type of peak."

        new_peak = self.VALID_TYPE_PEAKS[peak_type](peak_name, peak_elevation)
        self.peaks.append(new_peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    # def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int) -> str:
    #     try:
    #         peak = self.VALID_PEAKS_TYPES[peak_type](peak_name, peak_elevation)
    #     except KeyError:
    #         return f"{peak_type} is an unknown type of peak."
    #
    #     self.peaks.append(peak)
    #
    #     return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        searched_peak = next(filter(lambda p: peak_name == p.name, self.peaks))
        recommended_gear = set(searched_peak.get_recommended_gear())
        gear = set(gear)

        if recommended_gear.issubset(gear):
            return f"{climber_name} is prepared to climb {peak_name}."  # TODO: CARE only return a message

        searched_climber = next(filter(lambda c: climber_name == c.name, self.climbers))
        searched_climber.is_prepared = False

        return f"{climber_name} is not prepared to climb {peak_name}. " \
               f"Missing gear: {', '.join(sorted(recommended_gear - gear))}."

    # def perform_climbing(self, climber_name: str, peak_name: str):
    #
    #     try:
    #         climber = next(filter(lambda c: climber_name == c.name, self.climbers))
    #     except StopIteration:
    #         return f"Climber {climber_name} is not registered yet."
    #
    #     try:
    #         peak = next(filter(lambda p: peak_name == p.name, self.peaks))
    #     except StopIteration:
    #         return f"Peak {peak_name} is not part of the wish list."
    #
    #     if not climber.is_prepared:
    #         return f"{climber_name} will need to be better prepared next time."
    #
    #     if not climber.can_climb:
    #         climber.rest()
    #         return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."
    #
    #     climber.climb(peak)
    #     return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."
    def perform_climbing(self, climber_name: str, peak_name: str) -> str:
        try:
            climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        except StopIteration:
            return f"Climber {climber_name} is not registered yet."

        try:
            peak = next(filter(lambda p: p.name == peak_name, self.peaks))
        except StopIteration:
            return f"Peak {peak_name} is not part of the wish list."

        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        if not climber.can_climb():
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

        climber.climb(peak)

        return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

    def get_statistics(self):
        climbers_to_sort = [climber for climber in self.climbers if len(climber.conquered_peaks) > 0]
        sorted_climbers = sorted(climbers_to_sort, key=lambda x: (-len(x.conquered_peaks), x.name))

        conquered_peaks = set()
        for climber in self.climbers:
            for peak in climber.conquered_peaks:
                conquered_peaks.add(peak)

        result = "Total climbed peaks: " + str(len(conquered_peaks)) + "\n**Climber's statistics:**\n" \
                 + '\n'.join(str(climber) for climber in sorted_climbers)

        return result

    # def get_statistics(self) -> str:
    #     climbers_that_can_climb = filter(lambda c: len(c.conquered_peaks) > 0, self.climbers)
    #     climbers = sorted(climbers_that_can_climb, key=lambda c: (-len(c.conquered_peaks), c.name))
    #
    #     total_peaks_climbed = len({p for c in climbers for p in c.conquered_peaks})
    #
    #     return f"Total climbed peaks: {total_peaks_climbed}\n" + \
    #         "**Climber's statistics:**\n" + \
    #         "\n".join(str(c) for c in climbers)


# from typing import List
# from project 1& 2.peaks.base_peak import BasePeak
# from project 1& 2.climbers.base_climber import BaseClimber
# from project 1& 2.climbers.arctic_climber import ArcticClimber
# from project 1& 2.climbers.summit_climber import SummitClimber
# from project 1& 2.peaks.summit_peak import SummitPeak
# from project 1& 2.peaks.arctic_peak import ArcticPeak

#
# class SummitQuestManagerApp:
#     VALID_CLIMBER_TYPES = {
#         "ArcticClimber": ArcticClimber,
#         "SummitClimber": SummitClimber,
#     }
#
#     VALID_PEAKS_TYPES = {
#         "ArcticPeak": ArcticPeak,
#         "SummitPeak": SummitPeak,
#     }
#
#     def __init__(self):
#         self.peaks: List[BasePeak] = []
#         self.climbers: List[BaseClimber] = []
#
#     def register_climber(self, climber_type: str, climber_name: str) -> str:
#         try:
#             climber = self.VALID_CLIMBER_TYPES[climber_type](climber_name)
#         except KeyError:
#             return f"{climber_type} doesn't exist in our register."
#
#         try:
#             next(filter(lambda c: c.name == climber_name, self.climbers))
#             return f"{climber_name} has been already registered."
#         except StopIteration:
#             self.climbers.append(climber)
#             return f"{climber_name} is successfully registered as a {climber_type}."
#
#     def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int) -> str:
#         try:
#             peak = self.VALID_PEAKS_TYPES[peak_type](peak_name, peak_elevation)
#         except KeyError:
#             return f"{peak_type} is an unknown type of peak."
#
#         self.peaks.append(peak)
#
#         return f"{peak_name} is successfully added to the wish list as a {peak_type}."
#
#     def check_gear(self, climber_name: str, peak_name: str, gear: List[str]) -> str:
#         climber = next(filter(lambda c: c.name == climber_name, self.climbers))
#         peak = next(filter(lambda p: p.name == peak_name, self.peaks))
#
#         if gear == peak.get_recommended_gear():
#             return f"{climber_name} is prepared to climb {peak_name}."
#
#         climber.is_prepared = False
#
#         return (f"{climber_name} is not prepared to climb {peak_name}. "
#                 f"Missing gear: "
#                 f"{', '.join(g for g in sorted(peak.get_recommended_gear()) if g not in gear)}.")
#
#     def perform_climbing(self, climber_name: str, peak_name: str) -> str:
#         try:
#             climber = next(filter(lambda c: c.name == climber_name, self.climbers))
#         except StopIteration:
#             return f"Climber {climber_name} is not registered yet."
#
#         try:
#             peak = next(filter(lambda p: p.name == peak_name, self.peaks))
#         except StopIteration:
#             return f"Peak {peak_name} is not part of the wish list."
#
#         if not climber.is_prepared:
#             return f"{climber_name} will need to be better prepared next time."
#
#         if not climber.can_climb():
#             climber.rest()
#             return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."
#
#         climber.climb(peak)
#
#         return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."
#
#     def get_statistics(self) -> str:
#         climbers_that_can_climb = filter(lambda c: len(c.conquered_peaks) > 0, self.climbers)
#         climbers = sorted(climbers_that_can_climb, key=lambda c: (-len(c.conquered_peaks), c.name))
#
#         total_peaks_climbed = len({p for c in climbers for p in c.conquered_peaks})
#
#         return f"Total climbed peaks: {total_peaks_climbed}\n" + \
#                 "**Climber's statistics:**\n" + \
#                 "\n".join(str(c) for c in climbers)
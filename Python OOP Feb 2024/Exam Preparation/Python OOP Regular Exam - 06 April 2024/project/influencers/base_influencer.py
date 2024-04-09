from abc import ABC, abstractmethod
from typing import List

from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign


class BaseInfluencer(ABC):
    def __init__(self, username: str, followers: int, engagement_rate: float):
        self.username = username
        self.followers = followers
        self.engagement_rate = engagement_rate
        self.campaigns_participated: List[HighBudgetCampaign, LowBudgetCampaign] = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value.strip() == "":
            raise ValueError("Username cannot be empty or consist only of whitespace!")

        self.__username = value

    @property
    def followers(self):
        return self.__followers

    @followers.setter
    def followers(self, value):
        if not value >= 0:
            raise ValueError("Followers must be a non-negative integer!")

        self.__followers = value

    @property
    def engagement_rate(self):
        return self.__engagement_rate

    @engagement_rate.setter
    def engagement_rate(self, value):
        if not 0.0 <= value <= 5.0:
            raise ValueError("Engagement rate should be between 0 and 5.")

        self.__engagement_rate = value

    @abstractmethod
    def calculate_payment(self, campaign: BaseCampaign):
        pass

    @abstractmethod
    def reached_followers(self, campaign_type: str):
        pass

    def display_campaigns_participated(self):
        if len(self.campaigns_participated) == 0:
            return f"{self.username} has not participated in any campaigns."

        result = f"{self.__class__.__name__} :) {self.username} :) participated in the following campaigns:"

        for campaign in self.campaigns_participated:
            result += f"\n  - Campaign ID: {campaign.campaign_id}, Brand: {campaign.brand}, " \
                      f"Reached followers: {self.reached_followers(campaign.__class__.__name__)}"  # TODO: CARE HERE reached_followers method

        return result

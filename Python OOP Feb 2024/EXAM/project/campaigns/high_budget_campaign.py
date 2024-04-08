from typing import List

from project.campaigns.base_campaign import BaseCampaign


class HighBudgetCampaign(BaseCampaign):


    INIT_BUDGET = 5000.0

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, HighBudgetCampaign.INIT_BUDGET, required_engagement)


    def check_eligibility(self, engagement_rate: float):
        if engagement_rate >= self.required_engagement + 0.2 * self.required_engagement:
            return True

        return False


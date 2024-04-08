from typing import List

from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    VALID_INFLUENCERS = {
        "PremiumInfluencer": PremiumInfluencer,
        "StandardInfluencer": StandardInfluencer
    }

    VALID_CAMPAIGNS = {
        "HighBudgetCampaign": HighBudgetCampaign,
        "LowBudgetCampaign": LowBudgetCampaign
    }

    def __init__(self):
        self.influencers: List[PremiumInfluencer, StandardInfluencer] = []
        self.campaigns: List[HighBudgetCampaign, LowBudgetCampaign] = []  # TODO: Care here

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.VALID_INFLUENCERS.keys():
            return f"{influencer_type} is not an allowed influencer type."

        searched_influencer_username = [i.username for i in self.influencers if i.username == username]
        if searched_influencer_username:
            return f"{username} is already registered."

        new_influencer = self.VALID_INFLUENCERS[influencer_type](username, followers, engagement_rate)
        self.influencers.append(new_influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_CAMPAIGNS.keys():
            return f"{campaign_type} is not a valid campaign type."

        searched_campaign = [c.campaign_id for c in self.campaigns if c.campaign_id == campaign_id]
        if searched_campaign:
            return f"Campaign ID {campaign_id} has already been created."

        new_campaign = self.VALID_CAMPAIGNS[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(new_campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        try:
            influencer = next(filter(lambda i: i.username == influencer_username, self.influencers))
        except StopIteration:
            return f"Influencer '{influencer_username}' not found."

        try:
            campaign = next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns))
        except StopIteration:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        calculated_payment = influencer.calculate_payment(campaign)
        if calculated_payment > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= calculated_payment
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        total_reached_followers = {}

        for campaign in self.campaigns:
            total_followers = 0

            for influencer in campaign.participating_influencers:
                total_followers += influencer.reached_followers(campaign.__class__.__name__)
            if total_followers > 0:
                total_reached_followers[campaign] = total_followers

        return total_reached_followers

    def influencer_campaign_report(self, username: str):
        influencer = next((i for i in self.influencers if i.username == username), None)
        if influencer:
            return influencer.display_campaigns_participated()


    def campaign_statistics(self):
        sorted_campaigns = sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget))

        campaign_stats = []
        for campaign in sorted_campaigns:
            total_reached_followers = sum(influencer.reached_followers(campaign.__class__.__name__) for influencer in
                                          campaign.approved_influencers)
            campaign_info = f"  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, Total budget: ${campaign.budget:.2f}, Total reached followers: {total_reached_followers}"
            campaign_stats.append(campaign_info)

        statistics_str = "$$ Campaign Statistics $$\n" + "\n".join(campaign_stats)

        return statistics_str



    # # Helper methods
    # def _get_influencer(self, username: str):
    #     influencer = [i for i in self.influencers if i.username == username]
    #     return influencer[0] if influencer else None
    #
    # def _get_campaign(self, campaign_id: int):
    #     campaign = [c for c in self.campaigns if c.campaign_id == campaign_id]
    #     return campaign[0] if campaign else None
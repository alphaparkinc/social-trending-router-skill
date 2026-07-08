"""
social-trending-router-skill: Client SDK
Auto-adjusts social media campaign budgets based on keyword matching to viral topics.
"""
from __future__ import annotations
from typing import Optional


class SocialTrendingRouterClient:
    """
    SDK for dynamic budget routing.
    """

    def route_trends(
        self,
        trending_keywords: list[str],
        ad_campaigns: list[dict],
    ) -> dict:
        trends = [tk.lower() for tk in trending_keywords]
        routed = []

        for camp in ad_campaigns:
            cid = camp.get("id", "unknown")
            name = camp.get("name", "Unnamed")
            camp_kws = [ck.lower() for ck in camp.get("keywords", [])]
            base_b = float(camp.get("base_budget", 100.0))

            # Check for keyword overlap
            matches = list(set(trends).intersection(camp_kws))
            multiplier = 1.0 + (len(matches) * 0.50)  # Add 50% budget per matching trend

            routed.append({
                "id": cid,
                "name": name,
                "matching_trends": matches,
                "original_budget": base_b,
                "adjusted_budget": round(base_b * multiplier, 2),
                "multiplier": multiplier
            })

        return {
            "routed_campaigns": routed,
            "active_trends_detected": len(trends)
        }

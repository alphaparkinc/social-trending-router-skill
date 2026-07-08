"""
example_usage.py -- Demonstrates SocialTrendingRouterClient
"""
from client import SocialTrendingRouterClient

def main():
    client = SocialTrendingRouterClient()
    result = client.route_trends(
        trending_keywords=["skincare", "ecofriendly", "organic"],
        ad_campaigns=[
            {"id": "c1", "name": "Eco Serum Launch", "keywords": ["skincare", "organic"], "base_budget": 500},
            {"id": "c2", "name": "Heavy Duty Tech", "keywords": ["gadgets", "charge"], "base_budget": 200}
        ]
    )
    print("[Social Trending Router Result]")
    for c in result['routed_campaigns']:
        print(f"Campaign: {c['name']} | Multiplier: {c['multiplier']}x | Budget: ${c['adjusted_budget']}")

if __name__ == "__main__":
    main()

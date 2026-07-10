# genpark-social-trending-router-skill

> **GenPark AI Agent Skill** -- Viral topic ad budget router.

## Quick Start

```python
from client import SocialTrendingRouterClient
client = SocialTrendingRouterClient()
res = client.route_trends(["skincare"], [{"keywords": ["skincare"], "base_budget": 100}])
print(res["routed_campaigns"])
```

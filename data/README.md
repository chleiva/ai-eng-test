# Data Notes

## Catalog Schema
`data/catalog.jsonl` contains one product per line.

Each record uses this shape:

```json
{
  "tenant": "adidas",
  "product_id": "adidas-rs-001",
  "name": "TerraGrip WeatherRun",
  "category": "footwear",
  "description": "Stable running shoe with grippy outsole and weather-resistant upper for wet commutes and rainy-day training.",
  "price_gbp": 95.0,
  "attributes": {
    "best_for": ["running", "commute"],
    "foot_support": "high",
    "water_resistant": true,
    "vegan": false,
    "gluten_free": null,
    "lactose_free": null,
    "breakfast_friendly": false
  }
}
```

## Why The Data Looks Like This
The dataset is intentionally shaped to support:
- semantic search over rich product descriptions
- structured filtering by `tenant`, `price_gbp`, and `attributes`
- tradeoff discussion between keyword, vector, and hybrid retrieval

All provided records are synthetic and included for assessment purposes only.

## Important Behaviors The Data Supports
- Footwear queries where suitability is described indirectly, such as rainy weather, foot support, commute, or trail use
- Grocery queries where dietary constraints should rely on structured metadata, not just keywords
- Mixed-quality queries where budget, category, and suitability all matter
- Tenant isolation checks, since products across different tenants may sound similar

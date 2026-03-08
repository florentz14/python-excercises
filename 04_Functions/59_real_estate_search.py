# -------------------------------------------------
# File Name: 59_real_estate_search.py
# Description: Search properties by budget; price formula by zone
# -------------------------------------------------

PROPERTIES = [
    {"year": 2000, "meters": 100, "rooms": 3, "garage": True, "zone": "A"},
    {"year": 2012, "meters": 60, "rooms": 2, "garage": True, "zone": "B"},
    {"year": 1980, "meters": 120, "rooms": 4, "garage": False, "zone": "A"},
    {"year": 2005, "meters": 75, "rooms": 3, "garage": True, "zone": "B"},
    {"year": 2015, "meters": 90, "rooms": 2, "garage": False, "zone": "A"},
]


def compute_price(p: dict) -> float:
    """Base * age_factor. Zone B: base * 1.5."""
    base = p["meters"] * 1000 + p["rooms"] * 5000 + (15000 if p["garage"] else 0)
    age = 2025 - p["year"]
    age_factor = 1 - age / 100
    if p["zone"] == "A":
        return base * age_factor
    return base * age_factor * 1.5


def search_by_budget(properties: list[dict], budget: float) -> list[dict]:
    """Return properties with price <= budget, each with 'price' key added."""
    result = []
    for p in properties:
        price = compute_price(p)
        if price <= budget:
            result.append({**p, "price": round(price, 2)})
    return result


if __name__ == "__main__":
    print(search_by_budget(PROPERTIES, 150000))
    print(search_by_budget(PROPERTIES, 250000))

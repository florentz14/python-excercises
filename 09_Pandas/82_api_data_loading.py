# -------------------------------------------------
# File Name: 82_api_data_loading.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Loads JSON from API into DataFrame.
# -------------------------------------------------

import json
from pathlib import Path

import pandas as pd

# Simulate API response (avoids network dependency)
# In production: response = requests.get(url); data = response.json()
API_RESPONSE = {
    "users": [
        {"id": 1, "name": "Anna", "role": "admin"},
        {"id": 2, "name": "Bob", "role": "user"},
        {"id": 3, "name": "Carol", "role": "user"},
    ],
    "meta": {"total": 3, "page": 1},
}

# Parse JSON
data = API_RESPONSE["users"]
df = pd.DataFrame(data)

print("=== FROM JSON (simulated API) ===")
print(df)
print()

# With nested JSON
NESTED = [
    {"id": 1, "name": "A", "address": {"city": "NYC", "zip": "10001"}},
    {"id": 2, "name": "B", "address": {"city": "LA", "zip": "90001"}},
]
df_nested = pd.json_normalize(NESTED)
print("=== json_normalize (nested) ===")
print(df_nested)
print()

# Real API example (commented — needs requests)
# import requests
# r = requests.get("https://api.example.com/data")
# df = pd.DataFrame(r.json())

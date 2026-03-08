"""W3Resource 28: City Wise Count."""
import pandas as pd

# Sample dataset: city and name of person
data = {
    "city": [
        "California",
        "Georgia",
        "Los Angeles",
        "California",
        "Georgia",
        "Los Angeles",
        "California",
        "California",
        "Los Angeles",
        "Los Angeles",
    ],
    "name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack"],
}
df = pd.DataFrame(data)
result = df.groupby("city").size().reset_index(name="Number of people")
print(result)

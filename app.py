
import pandas as pd

data = [
    {"Nation": "United States", "Capital": "Washington, D.C.", "Head of State": "President"},
    {"Nation": "Canada", "Capital": "Ottawa", "Head of State": "Prime Minister"},
    {"Nation": "United Kingdom", "Capital": "London", "Head of State": "Monarch"},
    {"Nation": "France", "Capital": "Paris", "Head of State": "President"},
    {"Nation": "Germany", "Capital": "Berlin", "Head of State": "Federal President"},
    {"Nation": "Japan", "Capital": "Tokyo", "Head of State": "Emperor"},
    {"Nation": "Australia", "Capital": "Canberra", "Head of State": "Prime Minister"},
    {"Nation": "India", "Capital": "New Delhi", "Head of State": "President"},
    {"Nation": "Brazil", "Capital": "Brasília", "Head of State": "President"},
    {"Nation": "South Africa", "Capital": "Pretoria", "Head of State": "President"},
]

df = pd.DataFrame(data)
print(df.to_markdown(index=False))

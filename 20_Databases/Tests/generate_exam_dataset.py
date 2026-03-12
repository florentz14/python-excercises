"""
File: generate_exam_dataset.py
Description: Generate a realistic exam dataset for Pandas practice
Python: 3.14+
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from pathlib import Path

# ------------------------------
# Sample data pools
# ------------------------------

names = [
"Aisha Hassan","Mateo Rodriguez","Hiroshi Tanaka","Kwame Mensah","Sofia Petrova",
"Liam OConnor","Fatima Alzahra","Chen Wei","Amir Rahimi","Ananya Sharma",
"Lucas Silva","Noah Johnson","Diego Fernandez","Yuki Nakamura","Omar Haddad",
"Alejandro Cruz","Zara Khan","Ivan Ivanov","Samuel Okafor","Emma Williams",
"Mei Lin","Priya Patel","Carlos Gutierrez","Sara Svensson","Ali Demir",
"Victor Dubois","Laura Garcia","Daniel Kim","Chloe Martin","Pedro Alvarez"
]

countries = [
"USA","Mexico","Brazil","India","China","Japan","Nigeria","Spain",
"Egypt","Canada","Germany","France","Argentina","Chile","Peru",
"Pakistan","Turkey","Russia","Sweden","Philippines"
]

subjects = [
"Mathematics",
"Physics",
"Computer Science",
"Statistics",
"Data Science",
"Cybersecurity",
"Networking",
"Algorithms"
]

genders = ["Male","Female"]

# ------------------------------
# Generate dataset
# ------------------------------

records = []

for i in range(1000):

    name = random.choice(names)
    country = random.choice(countries)
    subject = random.choice(subjects)
    gender = random.choice(genders)

    age = random.randint(18,30)
    study_hours = round(random.uniform(1,20),1)
    attempts = random.randint(1,3)

    score = round(random.uniform(5,20),1)

    # introduce missing values
    if random.random() < 0.05:
        score = np.nan

    qualify = "yes" if score >= 12 else "no"

    exam_date = datetime(2025,1,1) + timedelta(days=random.randint(0,365))

    records.append([
        i+1,
        name,
        country,
        gender,
        age,
        subject,
        study_hours,
        attempts,
        score,
        qualify,
        exam_date
    ])

columns = [
"student_id",
"name",
"country",
"gender",
"age",
"subject",
"study_hours",
"attempts",
"score",
"qualify",
"exam_date"
]

df = pd.DataFrame(records, columns=columns)

# ------------------------------
# Save dataset
# ------------------------------

BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent.parent
OUTPUT_DIR = PROJECT_ROOT / "09_Pandas" / "data"
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
OUTPUT_FILE = OUTPUT_DIR / f"students_exam_dataset_{timestamp}.csv"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_FILE, index=False)

print("Dataset created successfully!")
print(f"Saved to: {OUTPUT_FILE}")
print(df.head())
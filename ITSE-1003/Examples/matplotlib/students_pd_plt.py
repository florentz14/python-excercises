import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

# Load the data from the CSV file
DATA_DIR = Path(__file__).resolve().parent.parent / "data"

# read the csv file
df = pd.read_csv(DATA_DIR / "studentsG.csv")

# Plot the data
df.plot(kind="bar", x="Name", y="Grade")

# Set the title and labels
plt.title("Final Grade by Student")
plt.xlabel("Student Name")
plt.ylabel("Grade")

# Show the plot
plt.show()

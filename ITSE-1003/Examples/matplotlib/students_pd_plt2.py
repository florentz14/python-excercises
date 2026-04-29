import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

# Load the data from the CSV file
DATA_DIR = Path(__file__).resolve().parent.parent / "data"

# read the csv file
df = pd.read_csv(DATA_DIR / "studentsG.csv")

# plot the data
df.plot(kind="bar", x="Name", y="Grade")

# set the title and labels
plt.title("Final Grade by Student")

# set the x labels
plt.xlabel("Student Name")

# set the y label
plt.ylabel("Grade")

# show the plot
# plt.show()

# improve the with formatting

# Plot the data with improved formatting
df.plot(kind="bar", x="Name", y="Grade",
        color="orange", edgecolor="black", legend=False)

# Set the title and labels with improved formatting
plt.title("Final Grade by Student", fontsize=14, fontweight="bold")
plt.xlabel("Student Name", fontsize=12)
plt.ylabel("Grade", fontsize=12)

# Set y-axis limits and rotate x-axis labels
plt.ylim(0, 100)

# Rotate x-axis labels and set font size
plt.xticks(rotation=45, fontsize=10)

# Add a grid for better readability
plt.grid(axis="y", alpha=0.3)

# Adjust layout to prevent clipping of labels
plt.tight_layout()

# Show the plot
plt.show()

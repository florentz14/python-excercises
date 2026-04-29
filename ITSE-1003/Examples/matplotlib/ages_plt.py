import matplotlib.pyplot as plt

# Create data for the histogram
ages = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]

# Create the histogram
plt.figure(figsize=(8, 5))

# Create the histogram with custom styling
plt.hist(ages, bins=5, color="steelblue", edgecolor="yellow", alpha=0.8)

# Add labels and title
plt.title("Ages of Students")
plt.xlabel("Age")
plt.ylabel("Frequency")

# Show the plot
plt.show()

'''
bins: means the number of bars in the histogram
color: means the color of the bars
edgecolor: means the color of the edges of the bars
title: means the title of the histogram
xlabel: means the label of the x-axis
ylabel: means the label of the y-axis
show: means to show the histogram
alpha: means the transparency of the bars
'''

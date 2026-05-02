import matplotlib.pyplot as plt
import statistics as stats

# create a list of numeric data
data = [12, 15, 15, 18, 20, 22, 22, 22, 25, 30]

# create x-values from 1 to the length of the data
x = list(range(1, len(data) + 1))

# calculate the average, also called the mean
average_value = stats.mean(data)

# calculate the median middle value
median_value = stats.median(data)

# calculate the mode, the most repeated value
mode_value = stats.mode(data)

# create a bar plot using x and data
plt.bar(x, data, label="DATA", color="#4287f5")

# Draw a horizontal line showing the average
plt.axhline(y=average_value, color="#FF0000", linestyle="--", label=f"Mean: {average_value}")
plt.axhline(y=median_value,  color="#00FF00", linestyle=":",  label=f"Median: {median_value}")
plt.axhline(y=mode_value,    color="#FFA500", linestyle="-.", label=f"Mode: {mode_value}")

# Add labels and title
plt.title("Data Analysis - Mean, Median & Mode (Bar Chart)")
plt.xlabel("Index")
plt.ylabel("Value")

# Show legend
plt.legend()

# Show grid for better readability
plt.grid(True, linestyle="--", alpha=0.5)

# Display the plot
plt.tight_layout()
plt.show()


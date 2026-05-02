import matplotlib.pyplot as plt
import statistics as stats

# create a list of numeric data
data = [12, 15, 15, 18, 20, 22, 22, 22, 25, 30]

# calculate the average, also called the mean
average_value = stats.mean(data)

# calculate the median middle value
median_value = stats.median(data)

# calculate the mode, the most repeated value
mode_value = stats.mode(data)

# create a histogram
plt.hist(data, bins=8, alpha=0.7, color="#4287f5", label="DATA", edgecolor="black")

# Draw vertical lines showing the statistics
plt.axvline(x=average_value, color="#FF0000", linestyle="--", linewidth=2, label=f"Mean: {average_value}")
plt.axvline(x=median_value,  color="#00FF00", linestyle=":",  linewidth=2, label=f"Median: {median_value}")
plt.axvline(x=mode_value,    color="#FFA500", linestyle="-.", linewidth=2, label=f"Mode: {mode_value}")

# Add labels and title
plt.title("Data Analysis - Mean, Median & Mode (Histogram)")
plt.xlabel("Value")
plt.ylabel("Frequency")

# Show legend
plt.legend()

# Show grid for better readability
plt.grid(True, linestyle="--", alpha=0.3)

# Add text annotations for statistics
plt.text(average_value + 0.5, plt.ylim()[1] * 0.9, f"Mean: {average_value}", 
         rotation=0, ha='left', color="#FF0000", fontweight='bold')
plt.text(median_value + 0.5, plt.ylim()[1] * 0.8, f"Median: {median_value}", 
         rotation=0, ha='left', color="#00FF00", fontweight='bold')
plt.text(mode_value + 0.5, plt.ylim()[1] * 0.7, f"Mode: {mode_value}", 
         rotation=0, ha='left', color="#FFA500", fontweight='bold')

# Display the plot
plt.tight_layout()
plt.show()

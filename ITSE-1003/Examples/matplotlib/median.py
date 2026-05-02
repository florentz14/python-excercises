import matplotlib.pyplot as plt

import numpy as np
import statistics as stats

# Sample data
data = [12, 15, 15, 18, 20, 22, 22, 22, 25, 30]

# Create x-values from 1 to the length of the data
x = list(range(1, len(data) + 1))

# Calculate median
median = stats.median(data)

# Calculate mode
mode = stats.mode(data)

# calculate mean
mean = stats.mean(data)

# Create the plot
plt.plot(x, data, label='Data', marker='o')

# Add median line
plt.axhline(median, color='r', linestyle='--', label=f'Median: {median}')

# Add mode line
plt.axhline(mode, color='g', linestyle=':', label=f'Mode: {mode}')

# Add mean line
plt.axhline(mean, color='b', linestyle='-.', label=f'Mean: {mean}')

# Add labels and legend
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Median, Mode and Mean')

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Show legend
plt.legend()

# Show the plot
plt.show()

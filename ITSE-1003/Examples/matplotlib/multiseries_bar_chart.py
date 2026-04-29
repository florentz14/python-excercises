import matplotlib.pyplot as plt
import numpy as np

# Create the x-axis values
index = np.arange(5)

# Create three series of values
values1 = [5, 7, 3, 4, 6]
values2 = [6, 6, 4, 5, 7]
values3 = [5, 6, 5, 4, 6]

# Set bar width
bw = 0.3

# Set axis limits
plt.axis((0, 5, 0, 8))

# Set title
plt.title('A Multiseries Bar Chart', fontsize=20)

# Create bars for each series
plt.bar(index, values1, bw, color='b')
plt.bar(index + bw, values2, bw, color='g')
plt.bar(index + 2*bw, values3, bw, color='r')

# Set x-axis labels
plt.xticks(index + 1.5*bw, ['A', 'B', 'C', 'D', 'E'])

plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.show()

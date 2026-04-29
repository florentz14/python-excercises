import matplotlib.pyplot as plt

# Set axis limits
plt.axis((0, 5, 0, 20))

# Set title and labels
plt.title('My first plot', fontsize=20, fontname='Times New Roman')
plt.xlabel('Counting', color='gray')
plt.ylabel('Square values', color='gray')

# Plot the points and add text annotations
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')

# Add text annotations for each point
plt.text(1, 1.5, 'First')
plt.text(2, 4.5, 'Second')
plt.text(3, 9.5, 'Third')
plt.text(4, 16.5, 'Fourth')
plt.text(1.1, 12, r'$y = x^2$', fontsize=20, bbox={
         'facecolor': 'yellow', 'alpha': 0.2})

# Add a grid to the plot
plt.grid(True)

# Display the plot
plt.show()

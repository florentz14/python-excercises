import matplotlib.pyplot as plt

# Create data for the scatter plot
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Create the scatter plot
plt.scatter(x, y)

# Add labels and title
plt.title("Scatter Plot")
plt.xlabel("Dimensionality of the data")
plt.ylabel("Value of the data")

# Show the plot
plt.show()

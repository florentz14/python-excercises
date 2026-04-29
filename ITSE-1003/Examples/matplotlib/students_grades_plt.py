import matplotlib.pyplot as plt

# Create data for the bar chart
students = ["John", "Jane", "Jim", "Jill"]
grades = [85, 90, 78, 92]

# Create the bar chart
plt.figure(figsize=(8, 5))

# Create the bar chart
plt.bar(students, grades)

# Add labels and title
plt.title("Student Grades")
plt.xlabel("Student")
plt.ylabel("Grade")

# Rotate the x-axis labels
plt.xticks(rotation=45)

# Show the plot
plt.show()

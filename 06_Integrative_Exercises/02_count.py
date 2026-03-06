# Initialize and display student count
students_count = 1000
print("Number of students:", students_count)

# Update the student count by adding 5 new students
students_count += 5
print("Updated number of students:", students_count)

# Store and display the average score
average_score = 85.5
print("Average score:", average_score)

# Track enrollment status
is_enrolled = True
print("Is enrolled:", is_enrolled)

# Store course information
course_name = "Introduction to Python"
print("Course name:", course_name)

print(len(course_name))  # Display the length of the course name
print(course_name.upper())  # Display the course name in uppercase
print(course_name.lower())  # Display the course name in lowercase
print(course_name[0:11])  # Display the first 11 characters of the course name
# Replace "Python" with "Programming"
print(course_name.replace("Python", "Programming"))
print(course_name.find("Python"))  # Find the starting index of "Python"
print(course_name.split(" "))  # Split the course name into a list of words
# Check if the course name starts with "Intro"
print(course_name.startswith("Intro"))
# Check if the course name ends with "Python"
print(course_name.endswith("Python"))
print(course_name[0])  # Display the first character of the course name
print(course_name[-1])  # Display the last character of the course name
print(course_name[0::2])  # Display every second character of the course name
print(course_name[::-1])  # Display the course name in reverse order
# Display the first three characters of the course name
print(course_name[0:3])
print(course_name[3:6])  # Display characters from index 3 to 5
print(course_name[0:])  # Display the entire course name
print(course_name[:3])  # Display the first three characters of the course name
print(course_name[:])  # Display the entire course name
print(course_name.count("o"))  # Count occurrences of the letter "o"
# Check if the course name contains only alphabetic characters
print(course_name.isalpha())


# Create and display a welcome greeting
greeting = "Welcome to the course!"
print(greeting)

# Combine multiple strings to create a full enrollment message
full_message = greeting + " You are enrolled in " + course_name + "."
print(full_message)

# -------------------------------------------------
# File Name: 03_exam_grades.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming
# Professor: Mauricio Quiroga
# Date: Module 06 Lab
# Description: Exam Grades Program. Dr. LaClaire gives a series of exams
#              during the semester in her chemistry class. At the end of the
#              semester, she drops each student's lowest test score before
#              averaging the scores. The program reads a student's test
#              scores as input and calculates the average with the lowest
#              score dropped.
# -------------------------------------------------

# =============================================================================
# EXERCISE 3: Exam Grades Program
# =============================================================================

print("=" * 60)
print("EXERCISE 3: Exam Grades Program")
print("=" * 60)

# Initialize list to store test scores
test_scores = []

# Get test scores from user
# Try-except block: Handles exceptions that may occur during input conversion
try:
    print("Enter test scores (enter -1 to finish):")

    # Loop (while True): Continuously prompts until user enters -1 to finish
    while True:
        try:
            score = float(input("  Enter a test score (or -1 to finish): "))

            if score == -1:
                # User entered -1 to finish entering scores
                break  # Exit the loop
            elif score < 0 or score > 100:
                # Validate score range
                print(
                    "    Error: Test score must be between 0 and 100. Please try again.")
                continue  # Continue loop to ask for input again
            else:
                test_scores.append(score)  # Add score to the list
                print(
                    f"    Score {score} added. Total scores: {len(test_scores)}")

        except ValueError:
            # Handle invalid numeric input (e.g., non-numeric characters)
            print("    Error: Please enter a valid number.")

    # Process test scores
    if len(test_scores) < 2:
        print("\nError: You must enter at least 2 test scores to calculate average with lowest dropped.")
    else:
        # Display all scores
        print(f"\nAll test scores entered: {test_scores}")

        # Find and remove lowest score
        lowest_score = min(test_scores)  # Find the lowest score
        scores_without_lowest = test_scores.copy()  # Create a copy of the list
        scores_without_lowest.remove(lowest_score)  # Remove the lowest score

        # Calculate average with lowest score dropped
        average_without_lowest = sum(
            scores_without_lowest) / len(scores_without_lowest)

        # Display results
        print("\n" + "=" * 60)
        print("EXAM GRADES ANALYSIS")
        print("=" * 60)
        print(f"Number of test scores: {len(test_scores)}")
        print(f"All test scores: {test_scores}")
        print(f"Lowest score (dropped): {lowest_score}")
        print(f"Scores used for average: {scores_without_lowest}")
        print(
            f"Average with lowest score dropped: {average_without_lowest:.2f}")

        # Calculate average with all scores for comparison
        average_with_all = sum(test_scores) / len(test_scores)
        print(
            f"\nAverage with all scores (for comparison): {average_with_all:.2f}")

except Exception as e:
    # Handle any other unexpected errors
    print(f"Error: {e}")

print()

# =============================================================================
# CITATIONS
# =============================================================================
print("Citations:")
print("1. List Operations in Python:")
print("   - min() function for list analysis")
print("   - List methods: append(), remove(), copy()")
print("   Source: Python Documentation - Built-in Functions")
print("   https://docs.python.org/3/library/functions.html")
print()
print("2. Statistical Calculations:")
print("   - Average = Sum of values / Number of values")
print("   - Dropping lowest score before averaging")
print("   Source: Standard statistical methods for grade calculation")

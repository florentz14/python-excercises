# -------------------------------------------------
# File Name: 03_test_average_and_grade.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming
# Professor: Mauricio Quiroga
# Date: Module 05 Lab
# Description: Calculate test average and determine letter grades.
# -------------------------------------------------

# Calculate average of five test scores
def calc_average(score1: float, score2: float, score3: float, score4: float, score5: float) -> float:
    return (score1 + score2 + score3 + score4 + score5) / 5


# Determine letter grade based on score
def determine_grade(score: float) -> str:
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


print("=" * 60)
print("EXERCISE 3: Test Average and Grade")
print("=" * 60)

# Get user input
score1 = float(input("Enter test score 1: "))
score2 = float(input("Enter test score 2: "))
score3 = float(input("Enter test score 3: "))
score4 = float(input("Enter test score 4: "))
score5 = float(input("Enter test score 5: "))

# Validate scores
scores = [score1, score2, score3, score4, score5]
if any(score < 0 or score > 100 for score in scores):
    print("Error: Test scores must be between 0 and 100.")
else:
    # Calculate average
    average = calc_average(score1, score2, score3, score4, score5)
    
    # Display results
    print(f"\nTest Score\t\tLetter Grade")
    print("-" * 40)
    print(f"Score 1: {score1:.2f}\t\t{determine_grade(score1)}")
    print(f"Score 2: {score2:.2f}\t\t{determine_grade(score2)}")
    print(f"Score 3: {score3:.2f}\t\t{determine_grade(score3)}")
    print(f"Score 4: {score4:.2f}\t\t{determine_grade(score4)}")
    print(f"Score 5: {score5:.2f}\t\t{determine_grade(score5)}")
    print("-" * 40)
    print(f"Average Score: {average:.2f}\t\t{determine_grade(average)}")

print()

print("\n" + "=" * 60)
print("CITATION")
print("=" * 60)
print("1. Grade Calculation:")
print("   - Standard letter grade scale (A-F)")
print("   Source: Common grading scale used in educational institutions")

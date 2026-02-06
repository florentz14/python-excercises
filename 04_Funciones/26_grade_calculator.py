# -------------------------------------------------
# File Name: 04_26_grade_calculator.py
# Author: Florentino Báez
# Date: Module 04 - Exercise 26
# Description: Grade Calculator Program.
#              Convert numeric scores to letter grades.
#              Includes a while loop for multiple grade calculations.
# -------------------------------------------------

def get_grade(score: float) -> str:
    if score >= 90.0:
        return "A"
    elif score >= 80.0:
        return "B"
    elif score >= 70.0:
        return "C"
    elif score >= 60.0:
        return "D"
    else:
        return "F"


def main() -> None:
    while True:
        print("\nGrade Calculator")
        print("-" * 20)
        print("1. Calculate Grade")
        print("2. Exit")
        
        try:
            choice = input("Enter your choice (1 or 2): ")
            
            if choice == "1":
                score_input = input("Enter numeric score (0-100): ")
                score = float(score_input)
                
                if score < 0 or score > 100:
                    print("Error: Score must be between 0 and 100.")
                    continue
                
                grade = get_grade(score)
                print(f"Score: {score:.1f} -> Grade: {grade}")
                
            elif choice == "2":
                print("Goodbye!")
                break
                
            else:
                print("Error: Please enter 1 or 2.")
                
        except ValueError:
            print("Error: Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

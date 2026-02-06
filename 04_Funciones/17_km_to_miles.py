# -------------------------------------------------
# File Name: exercise_17_km_to_miles.py
# Author: Florentino Báez
# Date: Module 04 - Exercise 17
# Description: Distance Converter Program.
#              Convert between kilometers and miles using functions.
#              Includes a while loop for multiple conversions.
# -------------------------------------------------

def km_to_miles(kilometers: float) -> float:
    conversion_factor = 0.621371
    miles = kilometers * conversion_factor
    return miles


def miles_to_km(miles: float) -> float:
    conversion_factor = 1.60934
    kilometers = miles * conversion_factor
    return kilometers


def main() -> None:
    while True:
        print("\nDistance Converter")
        print("-" * 20)
        print("1. Kilometers to Miles")
        print("2. Miles to Kilometers")
        print("3. Exit")
        
        try:
            choice = input("Enter your choice (1, 2, or 3): ")
            
            if choice == "1":
                km_input = input("Enter distance in kilometers: ")
                kilometers = float(km_input)
                miles = km_to_miles(kilometers)
                print(f"{kilometers} kilometers = {miles:.4f} miles")
                
            elif choice == "2":
                miles_input = input("Enter distance in miles: ")
                miles = float(miles_input)
                kilometers = miles_to_km(miles)
                print(f"{miles} miles = {kilometers:.4f} kilometers")
                
            elif choice == "3":
                print("Goodbye!")
                break
                
            else:
                print("Error: Please enter 1, 2, or 3.")
                
        except ValueError:
            print("Error: Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

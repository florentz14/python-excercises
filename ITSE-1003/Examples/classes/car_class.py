# -------------------------------------------------
# File Name: car_class.py
# Author: Florentino
# Date: 3/20/26
# Description: Car class using Object-Oriented Programming concepts.
#              Includes brand, model, year, speed attributes and methods.
# -------------------------------------------------

class Car:
    """A simple Car class demonstrating OOP concepts."""
    
    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Initialize a Car object.
        
        Args:
            brand (str): The car manufacturer
            model (str): The car model name
            year (int): The manufacturing year
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0  # Default speed is 0
    
    def accelerate(self) -> None:
        """Increase speed by 10."""
        self.speed += 10
        print(f"{self.brand} {self.model} accelerated. Speed: {self.speed} km/h")
    
    def brake(self) -> None:
        """Decrease speed by 10 (not below 0)."""
        if self.speed >= 10:
            self.speed -= 10
            print(f"{self.brand} {self.model} braked. Speed: {self.speed} km/h")
        else:
            self.speed = 0
            print(f"{self.brand} {self.model} stopped. Speed: {self.speed} km/h")
    
    def display_speed(self) -> None:
        """Print current speed."""
        print(f"{self.brand} {self.model} current speed: {self.speed} km/h")
    
    def is_fast(self) -> None:
        """Check if car is fast (speed > 50)."""
        if self.speed > 50:
            print(f"This car is fast! 🚀")
        else:
            print(f"This car is not fast yet. 🐌")
    
    def get_info(self) -> str:
        """Get car information as a formatted string."""
        return f"{self.year} {self.brand} {self.model}"

    def check_gas(self) -> None:
        """Check if car has enough gas."""
        if self.speed > 0:
            print(f"{self.brand} {self.model} has enough gas.")
        else:
            print(f"{self.brand} {self.model} is out of gas.")
    
    def old_car(self) -> None:
        """Check if car is old (year < 2020)."""
        if self.year < 2020:
            print(f"{self.brand} {self.model} is old.")
        else:
            print(f"{self.brand} {self.model} is new.")
def main():
    """Main function to test the Car class."""
    print("=== Car Class Demo ===\n")
    
    # Create 3 different cars
    car1 = Car("Tesla", "Model S", 2023)
    car2 = Car("Toyota", "Camry", 2022)
    car3 = Car("Ford", "Mustang", 2024)
    
    print("Created 3 cars:")
    print(f"1. {car1.get_info()}")
    print(f"2. {car2.get_info()}")
    print(f"3. {car3.get_info()}")
    print()
    
    # Test car1 - Tesla
    print("=== Testing Tesla Model S ===")
    car1.accelerate()
    car1.display_speed()
    car1.accelerate()
    car1.display_speed()
    car1.accelerate()
    car1.display_speed()
    car1.accelerate()
    car1.display_speed()
    car1.accelerate()
    car1.display_speed()
    car1.accelerate()
    car1.display_speed()
    car1.is_fast()
    print()
    
    # Test car2 - Toyota
    print("=== Testing Toyota Camry ===")
    car2.accelerate()
    car2.accelerate()
    car2.accelerate()
    car2.display_speed()
    car2.is_fast()
    car2.brake()
    car2.display_speed()
    car2.brake()
    car2.display_speed()
    car2.brake()
    car2.display_speed()
    car2.brake()
    car2.display_speed()
    car2.brake()
    car2.display_speed()
    print()
    
    # Test car3 - Ford Mustang (fast car)
    print("=== Testing Ford Mustang ===")
    for i in range(6):  # Accelerate 6 times to reach 60 km/h
        car3.accelerate()
    car3.display_speed()
    car3.is_fast()
    
    # Test braking below 0
    print("\n=== Testing Brake Limit ===")
    car3.brake()
    car3.display_speed()
    car3.brake()
    car3.display_speed()
    car3.brake()
    car3.display_speed()
    car3.brake()
    car3.display_speed()
    car3.brake()
    car3.display_speed()
    car3.brake()  # This should keep speed at 0
    car3.display_speed()
    car3.is_fast()
    
    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    main()

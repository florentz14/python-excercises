# -------------------------------------------------
# File: 09_method_override.py
# Description: Method overriding in inheritance.
#              Polymorphism through method overriding.
# -------------------------------------------------


class Vehicle:
    """Parent class - Vehicle."""

    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year

    def start(self) -> str:
        """Start the vehicle."""
        return f"The {self.year} {self.make} {self.model} is starting"

    def stop(self) -> str:
        """Stop the vehicle."""
        return f"The {self.year} {self.make} {self.model} is stopping"

    def drive(self) -> str:
        """Drive the vehicle."""
        return f"Driving the {self.make} {self.model}"

    def get_info(self) -> str:
        """Get vehicle information."""
        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):
    """Car class - overrides some methods."""

    def __init__(self, make: str, model: str, year: int, num_doors: int = 4) -> None:
        super().__init__(make, model, year)
        self.num_doors = num_doors
        self.fuel_type = "gasoline"

    def start(self) -> str:
        """Override start method for car."""
        return f"The {self.num_doors}-door {self.make} {self.model} is starting with a key"

    def drive(self) -> str:
        """Override drive method."""
        return f"Cruising down the highway in the {self.make} {self.model}"

    def honk(self) -> str:
        """Car-specific method."""
        return "Beep beep!"


class ElectricCar(Car):
    """Electric car - further overrides methods."""

    def __init__(self, make: str, model: str, year: int, battery_range: int) -> None:
        super().__init__(make, model, year, num_doors=4)
        self.fuel_type = "electric"
        self.battery_range = battery_range

    def start(self):
        """Override start for electric car."""
        return f"The electric {self.make} {self.model} is starting silently"

    def drive(self):
        """Override drive for electric car."""
        return f"Quietly driving the {self.make} {self.model} with {self.battery_range} miles range"

    def charge(self):
        """Electric car specific method."""
        return f"Charging the {self.make} {self.model}"


class Motorcycle(Vehicle):
    """Motorcycle class - different override."""

    def __init__(self, make: str, model: str, year: int, engine_cc: int) -> None:
        super().__init__(make, model, year)
        self.engine_cc = engine_cc

    def start(self) -> str:
        """Override start for motorcycle."""
        return f"The {self.engine_cc}cc {self.make} {self.model} is starting with a kick"

    def drive(self) -> str:
        """Override drive for motorcycle."""
        return f"Riding the {self.make} {self.model} on two wheels"

    def wheelie(self) -> str:
        """Motorcycle-specific method."""
        return f"Doing a wheelie on the {self.make} {self.model}!"


# Demonstration
if __name__ == "__main__":
    print("=== Method Override Demo ===\n")

    # Create different vehicles
    car = Car("Toyota", "Camry", 2020, 4)
    electric_car = ElectricCar("Tesla", "Model 3", 2023, 358)
    motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2021, 1200)

    vehicles = [car, electric_car, motorcycle]

    print("Vehicle information:")
    for vehicle in vehicles:
        print(f"  {vehicle.get_info()}")

    print("\nStarting vehicles (overridden methods):")
    for vehicle in vehicles:
        print(f"  {vehicle.start()}")

    print("\nDriving vehicles (overridden methods):")
    for vehicle in vehicles:
        print(f"  {vehicle.drive()}")

    print("\nStopping vehicles (inherited method):")
    for vehicle in vehicles:
        print(f"  {vehicle.stop()}")

    print("\nVehicle-specific actions:")
    print(f"  {car.honk()}")
    print(f"  {electric_car.charge()}")
    print(f"  {motorcycle.wheelie()}")

    print("\n=== Calling Parent Methods ===")

    # Using super() to call parent method
    class SportsCar(Car):
        def start(self):
            # Call parent method first
            parent_message = super().start()
            return f"{parent_message}... VROOM! (sports car mode)"

    sports_car = SportsCar("Ferrari", "488", 2023, 2)
    print(f"Sports car start: {sports_car.start()}")

    print("\n=== Method Resolution Order (MRO) ===")
    print(f"ElectricCar MRO: {ElectricCar.__mro__}")

    print("\n=== Key Concepts ===")
    print("- Method overriding: child provides different implementation")
    print("- super(): call parent method from overridden method")
    print("- Polymorphism: same method name, different behavior")
    print("- MRO: determines which method is called in multiple inheritance")

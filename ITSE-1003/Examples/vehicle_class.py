# -------------------------------------------------
# File Name: vehicle_class.py
# Author: Florentino
# Date: 3/20/26
# Description: Vehicle class demonstrating OOP concepts.
#              Loads fleet from data/vehicles.csv (Bike, Car, Truck rows).
# -------------------------------------------------

import csv
import re
from datetime import datetime
from pathlib import Path
from typing import List, Optional

from examples_paths import VEHICLES_CSV

class Vehicle:
    """A base Vehicle class demonstrating OOP concepts."""
    
    def __init__(self, make: str, model: str, year: int, color: str = "Black") -> None:
        """
        Initialize a Vehicle object.
        
        Args:
            make (str): The vehicle manufacturer
            model (str): The vehicle model name
            year (int): The manufacturing year
            color (str): The vehicle color (default: Black)
        """
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self._mileage = 0.0  # Protected attribute for mileage
        self._is_running = False  # Protected attribute for engine status
        self._fuel_level = 100.0  # Protected attribute for fuel (percentage)
    
    @property
    def mileage(self) -> float:
        """Get the current mileage (read-only property)."""
        return self._mileage
    
    @property
    def is_running(self) -> bool:
        """Get the engine status (read-only property)."""
        return self._is_running
    
    @property
    def fuel_level(self) -> float:
        """Get the current fuel level."""
        return self._fuel_level
    
    def start_engine(self) -> None:
        """Start the vehicle engine."""
        if not self._is_running:
            if self._fuel_level > 0:
                self._is_running = True
                print(f"The {self.make} {self.model} engine has started.")
            else:
                print("Cannot start engine: No fuel!")
        else:
            print(f"The {self.make} {self.model} engine is already running.")
    
    def stop_engine(self) -> None:
        """Stop the vehicle engine."""
        if self._is_running:
            self._is_running = False
            print(f"The {self.make} {self.model} engine has stopped.")
        else:
            print(f"The {self.make} {self.model} engine is already off.")
    
    def drive(self, distance: float) -> None:
        """Drive the vehicle for a specified distance."""
        if not self._is_running:
            print("Cannot drive: Engine is not running!")
            return
        
        if distance <= 0:
            print("Distance must be positive!")
            return
        
        if self._fuel_level <= 0:
            print("Cannot drive: No fuel!")
            return
        
        # Calculate fuel consumption (1% per 10 miles)
        fuel_consumed = distance / 10
        
        if fuel_consumed > self._fuel_level:
            print(f"Not enough fuel! Need {fuel_consumed:.1f}%, have {self._fuel_level:.1f}%")
            return
        
        self._mileage += distance
        self._fuel_level -= fuel_consumed
        print(f"Drove {distance:.1f} miles. Mileage: {self._mileage:.1f}, Fuel: {self._fuel_level:.1f}%")
    
    def refuel(self, amount: float) -> None:
        """Refuel the vehicle."""
        if amount <= 0:
            print("Fuel amount must be positive!")
            return
        
        if self._is_running:
            print("Cannot refuel while engine is running!")
            return
        
        self._fuel_level = min(100.0, self._fuel_level + amount)
        print(f"Refueled {amount:.1f}%. Current fuel level: {self._fuel_level:.1f}%")
    
    def honk(self) -> None:
        """Make the vehicle honk."""
        print(f"The {self.make} {self.model} goes: Beep beep!")
    
    def get_age(self) -> int:
        """Calculate the age of the vehicle."""
        current_year = datetime.now().year
        return current_year - self.year
    
    def get_info(self) -> str:
        """Get comprehensive vehicle information."""
        status = "running" if self._is_running else "off"
        return (f"{self.year} {self.make} {self.model} ({self.color}) - "
                f"Mileage: {self._mileage:.1f} miles, "
                f"Fuel: {self._fuel_level:.1f}%, "
                f"Engine: {status}, "
                f"Age: {self.get_age()} years")
    
    def __str__(self) -> str:
        """String representation of the vehicle."""
        return f"{self.year} {self.make} {self.model} ({self.color})"


class Bike(Vehicle):
    """A bicycle class inheriting from Vehicle."""
    
    def __init__(self, make: str, model: str, year: int, color: str = "Red", 
                 bike_type: str = "Mountain", gears: int = 21) -> None:
        """
        Initialize a Bike object.
        
        Args:
            make (str): The bike manufacturer
            model (str): The bike model name
            year (int): The manufacturing year
            color (str): The bike color (default: Red)
            bike_type (str): Type of bike (Mountain, Road, Hybrid, etc.)
            gears (int): Number of gears (default: 21)
        """
        super().__init__(make, model, year, color)
        self.bike_type = bike_type
        self.gears = gears
        self._current_gear = 1  # Protected attribute for current gear
        self._has_motor = False  # Bikes don't have motors by default
    
    @property
    def current_gear(self) -> int:
        """Get the current gear."""
        return self._current_gear
    
    def start_engine(self) -> None:
        """Override: Bikes don't have engines."""
        print(f"Bikes don't have engines! Just start pedaling your {self.make} {self.model}.")
    
    def stop_engine(self) -> None:
        """Override: Bikes don't have engines."""
        print(f"Bikes don't have engines to stop!")
    
    def drive(self, distance: float) -> None:
        """Override: Bikes use human power, not fuel."""
        if distance <= 0:
            print("Distance must be positive!")
            return
        
        self._mileage += distance
        print(f"Pedaled {distance:.1f} miles. Mileage: {self._mileage:.1f} miles")
    
    def refuel(self, amount: float) -> None:
        """Override: Bikes don't need fuel."""
        print("Bikes don't need fuel! Just eat a good meal and rest.")
    
    def change_gear(self, new_gear: int) -> None:
        """Change the bike gear."""
        if 1 <= new_gear <= self.gears:
            self._current_gear = new_gear
            print(f"Changed to gear {new_gear}")
        else:
            print(f"Invalid gear! Use gears 1-{self.gears}")
    
    def ring_bell(self) -> None:
        """Ring the bike bell."""
        print(f"🔔 Ring ring! The {self.make} {self.model} bell is ringing!")
    
    def get_info(self) -> str:
        """Override: Add bike-specific information."""
        base_info = super().get_info()
        return (f"{base_info} (Bike: {self.bike_type}, "
                f"Gears: {self.gears}, Current gear: {self._current_gear})")


class Car(Vehicle):
    """A car class inheriting from Vehicle."""
    
    def __init__(self, make: str, model: str, year: int, color: str = "Black",
                 doors: int = 4, fuel_type: str = "Gasoline", 
                 transmission: str = "Automatic") -> None:
        """
        Initialize a Car object.
        
        Args:
            make (str): The car manufacturer
            model (str): The car model name
            year (int): The manufacturing year
            color (str): The car color (default: Black)
            doors (int): Number of doors (default: 4)
            fuel_type (str): Type of fuel (Gasoline, Diesel, Electric, Hybrid)
            transmission (str): Type of transmission (Automatic, Manual)
        """
        super().__init__(make, model, year, color)
        self.doors = doors
        self.fuel_type = fuel_type
        self.transmission = transmission
        self._trunk_open = False
    
    def open_trunk(self) -> None:
        """Open the car trunk."""
        if not self._trunk_open:
            self._trunk_open = True
            print(f"The trunk of the {self.make} {self.model} is now open.")
        else:
            print("The trunk is already open.")
    
    def close_trunk(self) -> None:
        """Close the car trunk."""
        if self._trunk_open:
            self._trunk_open = False
            print(f"The trunk of the {self.make} {self.model} is now closed.")
        else:
            print("The trunk is already closed.")
    
    def honk(self) -> None:
        """Override: Car horn sound."""
        print(f"The {self.make} {self.model} goes: Honk honk! 🚗")
    
    def get_info(self) -> str:
        """Override: Add car-specific information."""
        base_info = super().get_info()
        return (f"{base_info} (Car: {self.doors} doors, "
                f"{self.fuel_type}, {self.transmission})")


class Truck(Vehicle):
    """A truck class inheriting from Vehicle."""
    
    def __init__(self, make: str, model: str, year: int, color: str = "White",
                 cargo_capacity: float = 1000.0, num_wheels: int = 18) -> None:
        """
        Initialize a Truck object.
        
        Args:
            make (str): The truck manufacturer
            model (str): The truck model name
            year (int): The manufacturing year
            color (str): The truck color (default: White)
            cargo_capacity (float): Cargo capacity in pounds (default: 1000.0)
            num_wheels (int): Number of wheels (default: 18)
        """
        super().__init__(make, model, year, color)
        self.cargo_capacity = cargo_capacity
        self.num_wheels = num_wheels
        self._cargo_weight = 0.0  # Current cargo weight
        self._trailer_attached = False
    
    @property
    def cargo_weight(self) -> float:
        """Get current cargo weight."""
        return self._cargo_weight
    
    def attach_trailer(self) -> None:
        """Attach a trailer."""
        if not self._trailer_attached:
            self._trailer_attached = True
            print(f"Trailer attached to the {self.make} {self.model}.")
        else:
            print("Trailer is already attached.")
    
    def detach_trailer(self) -> None:
        """Detach the trailer."""
        if self._trailer_attached:
            if self._cargo_weight > 0:
                print("Cannot detach trailer with cargo still loaded!")
                return
            self._trailer_attached = False
            print(f"Trailer detached from the {self.make} {self.model}.")
        else:
            print("No trailer is attached.")
    
    def load_cargo(self, weight: float) -> None:
        """Load cargo onto the truck."""
        if weight <= 0:
            print("Cargo weight must be positive!")
            return
        
        if not self._trailer_attached:
            print("Cannot load cargo without a trailer!")
            return
        
        if self._cargo_weight + weight > self.cargo_capacity:
            print(f"Cannot load {weight:.1f} lbs! "
                  f"Current: {self._cargo_weight:.1f} lbs, "
                  f"Capacity: {self.cargo_capacity:.1f} lbs")
            return
        
        self._cargo_weight += weight
        print(f"Loaded {weight:.1f} lbs of cargo. "
              f"Total cargo: {self._cargo_weight:.1f} lbs")
    
    def unload_cargo(self, weight: Optional[float] = None) -> None:
        """Unload cargo from the truck."""
        if weight is None:
            # Unload all cargo
            if self._cargo_weight > 0:
                print(f"Unloaded {self._cargo_weight:.1f} lbs of cargo.")
                self._cargo_weight = 0.0
            else:
                print("No cargo to unload.")
        else:
            # Unload specific amount
            if weight <= 0:
                print("Unload weight must be positive!")
                return
            
            if weight > self._cargo_weight:
                print(f"Cannot unload {weight:.1f} lbs! "
                      f"Only have {self._cargo_weight:.1f} lbs loaded.")
                return
            
            self._cargo_weight -= weight
            print(f"Unloaded {weight:.1f} lbs of cargo. "
                  f"Remaining cargo: {self._cargo_weight:.1f} lbs")
    
    def honk(self) -> None:
        """Override: Truck horn sound."""
        print(f"The {self.make} {self.model} goes: HOOONK HOOONK! 🚚")
    
    def drive(self, distance: float) -> None:
        """Override: Trucks consume more fuel with cargo."""
        if not self._is_running:
            print("Cannot drive: Engine is not running!")
            return
        
        if distance <= 0:
            print("Distance must be positive!")
            return
        
        if self._fuel_level <= 0:
            print("Cannot drive: No fuel!")
            return
        
        # Trucks consume more fuel with cargo (1.5% per 10 miles + cargo penalty)
        base_consumption = distance / 10
        cargo_penalty = (self._cargo_weight / self.cargo_capacity) * 0.5
        fuel_consumed = base_consumption * (1 + cargo_penalty)
        
        if fuel_consumed > self._fuel_level:
            print(f"Not enough fuel! Need {fuel_consumed:.1f}%, have {self._fuel_level:.1f}%")
            return
        
        self._mileage += distance
        self._fuel_level -= fuel_consumed
        print(f"Drove {distance:.1f} miles with {self._cargo_weight:.1f} lbs cargo. "
              f"Mileage: {self._mileage:.1f}, Fuel: {self._fuel_level:.1f}%")
    
    def get_info(self) -> str:
        """Override: Add truck-specific information."""
        base_info = super().get_info()
        return (f"{base_info} (Truck: {self.num_wheels} wheels, "
                f"Capacity: {self.cargo_capacity:.1f} lbs, "
                f"Cargo: {self._cargo_weight:.1f} lbs)")


def _gears_from_transmission(transmission: str) -> int:
    m = re.match(r"(\d+)-Speed", transmission.strip())
    return int(m.group(1)) if m else 21


def _bike_type_from_row(special: str) -> str:
    s = special.strip()
    if "Mountain" in s:
        return "Mountain"
    if "Road" in s or "Carbon" in s:
        return "Road"
    return "Hybrid"


def vehicle_from_csv_row(row: dict) -> Vehicle:
    """Build a Bike, Car, or Truck from one row of data/vehicles.csv."""
    vtype = row["Vehicle_Type"].strip()
    make = row["Make"].strip()
    model = row["Model"].strip()
    year = int(row["Year"])
    color = row["Color"].strip()

    if vtype.lower() == "bike":
        gears = _gears_from_transmission(row["Transmission"])
        return Bike(
            make,
            model,
            year,
            color,
            _bike_type_from_row(row.get("Special_Features", "")),
            gears,
        )

    if vtype.lower() == "car":
        doors = int(row["Doors"]) if str(row.get("Doors", "")).isdigit() else 4
        return Car(
            make,
            model,
            year,
            color,
            doors,
            row["Fuel_Type"].strip(),
            row["Transmission"].strip(),
        )

    if vtype.lower() == "truck":
        wheels = int(row["Wheels"]) if str(row.get("Wheels", "")).isdigit() else 18
        return Truck(make, model, year, color, 2000.0, wheels)

    return Car(make, model, year, color)


def load_vehicles_from_csv(csv_path: Optional[Path] = None) -> List[Vehicle]:
    """Load all rows from data/vehicles.csv into Vehicle instances."""
    path = csv_path or VEHICLES_CSV
    if not path.is_file():
        raise FileNotFoundError(path)
    with path.open(encoding="utf-8", newline="") as f:
        return [vehicle_from_csv_row(r) for r in csv.DictReader(f)]


def main():
    """Main function to test Vehicle inheritance."""
    print("=== Vehicle demo (data/vehicles.csv) ===\n")

    vehicles = load_vehicles_from_csv()
    print(f"Loaded {len(vehicles)} vehicles from CSV:\n")
    for vehicle in vehicles:
        print(f"- {vehicle.get_info()}")
    print()

    bike = next((v for v in vehicles if isinstance(v, Bike)), None)
    car = next((v for v in vehicles if isinstance(v, Car)), None)
    truck = next((v for v in vehicles if isinstance(v, Truck)), None)

    if not bike or not car or not truck:
        print("CSV must include at least one Bike, Car, and Truck row.")
        return

    # Test Bike
    print("=== Testing Bike (first in CSV) ===")
    print(bike.get_info())
    bike.start_engine()  # Override
    bike.drive(15)  # Override
    bike.change_gear(3)
    bike.ring_bell()
    bike.refuel(0)  # Override
    bike.stop_engine()  # Override
    print()

    # Test Car
    print("=== Testing Car (first in CSV) ===")
    print(car.get_info())
    car.start_engine()
    car.drive(50)
    car.open_trunk()
    car.honk()  # Override
    car.close_trunk()
    car.stop_engine()
    print()

    # Test Truck
    print("=== Testing Truck (first in CSV) ===")
    print(truck.get_info())
    truck.start_engine()
    truck.attach_trailer()
    truck.load_cargo(500)
    truck.load_cargo(800)
    truck.drive(100)  # Override with cargo penalty
    truck.honk()  # Override
    truck.unload_cargo(300)
    truck.unload_cargo()  # Unload all
    truck.detach_trailer()
    truck.stop_engine()
    print()
    
    # Display final status
    print("=== Final Vehicle Status ===")
    for vehicle in vehicles:
        print(vehicle.get_info())
    
    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    main()

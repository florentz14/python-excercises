# -------------------------------------------------
# File: 26_vehicle.py
# Description: Vehicle hierarchy - practical application.
#              Multiple inheritance, mixins, advanced OOP.
# -------------------------------------------------

from abc import ABC, abstractmethod
from typing import Optional
from datetime import datetime


class Vehicle(ABC):
    """Abstract base class for all vehicles."""

    def __init__(self, make: str, model: str, year: int, color: str = "black"):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self._mileage = 0
        self._is_running = False

    @property
    def mileage(self) -> int:
        """Get mileage."""
        return self._mileage

    @mileage.setter
    def mileage(self, value: int):
        """Set mileage with validation."""
        if not isinstance(value, int) or value < 0:
            raise ValueError("Mileage must be a non-negative integer")
        if value < self._mileage:
            raise ValueError("Cannot decrease mileage")
        self._mileage = value

    @abstractmethod
    def start_engine(self) -> str:
        """Start the vehicle engine."""
        pass

    @abstractmethod
    def stop_engine(self) -> str:
        """Stop the vehicle engine."""
        pass

    @abstractmethod
    def drive(self, miles: int) -> str:
        """Drive the vehicle for specified miles."""
        pass

    def get_info(self) -> str:
        """Get vehicle information."""
        status = "Running" if self._is_running else "Stopped"
        return f"{self.year} {self.make} {self.model} ({self.color}) - {self._mileage} miles - {status}"

    def __str__(self) -> str:
        """String representation."""
        return f"{self.year} {self.make} {self.model}"


class Engine:
    """Engine mixin for vehicles with engines."""

    def __init__(self, engine_type: str, horsepower: int):
        self.engine_type = engine_type
        self.horsepower = horsepower
        self._engine_running = False

    def start_engine(self) -> str:
        """Start the engine."""
        if self._engine_running:
            return "Engine is already running"
        self._engine_running = True
        return f"{self.engine_type} engine started ({self.horsepower} HP)"

    def stop_engine(self) -> str:
        """Stop the engine."""
        if not self._engine_running:
            return "Engine is already stopped"
        self._engine_running = False
        return f"{self.engine_type} engine stopped"

    def is_engine_running(self) -> bool:
        """Check if engine is running."""
        return self._engine_running


class ElectricMotor:
    """Electric motor mixin for electric vehicles."""

    def __init__(self, battery_capacity: float, range_miles: int):
        self.battery_capacity = battery_capacity  # kWh
        self.range_miles = range_miles
        self._charge_level = 100.0  # percentage
        self._motor_running = False

    def start_motor(self) -> str:
        """Start the electric motor."""
        if self._motor_running:
            return "Motor is already running"
        if self._charge_level <= 0:
            return "Battery is empty - cannot start motor"
        self._motor_running = True
        return f"Electric motor started ({self._charge_level:.1f}% charge)"

    def stop_motor(self) -> str:
        """Stop the electric motor."""
        if not self._motor_running:
            return "Motor is already stopped"
        self._motor_running = False
        return "Electric motor stopped"

    def charge_battery(self, hours: float) -> str:
        """Charge the battery."""
        if hours <= 0:
            raise ValueError("Charging time must be positive")

        # Simple charging model: 20% per hour
        charge_rate = 20.0  # percent per hour
        charge_added = min(hours * charge_rate, 100.0 - self._charge_level)
        self._charge_level += charge_added

        return f"Battery charged to {self._charge_level:.1f}% (+{charge_added:.1f}%)"

    def get_battery_status(self) -> str:
        """Get battery status."""
        return f"Battery: {self._charge_level:.1f}% ({self.battery_capacity * self._charge_level / 100:.1f} kWh remaining)"


class Car(Vehicle, Engine):
    """Car class using multiple inheritance."""

    def __init__(self, make: str, model: str, year: int, color: str = "black",
                 engine_type: str = "gasoline", horsepower: int = 200):
        Vehicle.__init__(self, make, model, year, color)
        Engine.__init__(self, engine_type, horsepower)
        self.fuel_efficiency = 25  # MPG

    def start_engine(self) -> str:
        """Start the car engine."""
        self._is_running = True
        return Engine.start_engine(self)

    def stop_engine(self) -> str:
        """Stop the car engine."""
        result = Engine.stop_engine(self)
        self._is_running = False
        return result

    def drive(self, miles: int) -> str:
        """Drive the car."""
        if not self._is_running:
            return "Cannot drive - engine is not running"

        if miles <= 0:
            raise ValueError("Miles must be positive")

        self._mileage += miles
        fuel_used = miles / self.fuel_efficiency

        return f"Drove {miles} miles. Fuel used: {fuel_used:.1f} gallons. Total mileage: {self._mileage}"

    def get_info(self) -> str:
        """Get car information."""
        info = Vehicle.get_info(self)
        info += f"\nEngine: {self.engine_type} ({self.horsepower} HP)"
        info += f"\nFuel Efficiency: {self.fuel_efficiency} MPG"
        return info


class ElectricCar(Vehicle, ElectricMotor):
    """Electric car using multiple inheritance."""

    def __init__(self, make: str, model: str, year: int, color: str = "white",
                 battery_capacity: float = 75.0, range_miles: int = 250):
        Vehicle.__init__(self, make, model, year, color)
        ElectricMotor.__init__(self, battery_capacity, range_miles)
        self.efficiency = 3.5  # kWh per 100 miles

    def start_engine(self) -> str:
        """Start the electric car."""
        self._is_running = True
        return ElectricMotor.start_motor(self)

    def stop_engine(self) -> str:
        """Stop the electric car."""
        result = ElectricMotor.stop_motor(self)
        self._is_running = False
        return result

    def drive(self, miles: int) -> str:
        """Drive the electric car."""
        if not self._is_running:
            return "Cannot drive - motor is not running"

        if miles <= 0:
            raise ValueError("Miles must be positive")

        # Calculate energy required
        energy_required = (miles / 100) * self.efficiency

        # Check if enough battery
        energy_available = (self._charge_level / 100) * self.battery_capacity
        if energy_required > energy_available:
            max_miles = (energy_available / self.efficiency) * 100
            return f"Insufficient battery. Can drive maximum {max_miles:.1f} miles."

        # Update battery and mileage
        self._charge_level -= (energy_required / self.battery_capacity) * 100
        self._mileage += miles

        return f"Drove {miles} miles. Energy used: {energy_required:.1f} kWh. Battery: {self._charge_level:.1f}%. Total mileage: {self._mileage}"

    def get_info(self) -> str:
        """Get electric car information."""
        info = Vehicle.get_info(self)
        info += f"\nBattery: {self.battery_capacity} kWh ({self.range_miles} miles range)"
        info += f"\n{self.get_battery_status()}"
        info += f"\nEfficiency: {self.efficiency} kWh/100 miles"
        return info


class HybridCar(Vehicle, Engine, ElectricMotor):
    """Hybrid car using multiple inheritance from both engine types."""

    def __init__(self, make: str, model: str, year: int, color: str = "silver",
                 engine_type: str = "gasoline", horsepower: int = 150,
                 battery_capacity: float = 12.0, electric_range: int = 50):
        Vehicle.__init__(self, make, model, year, color)
        Engine.__init__(self, engine_type, horsepower)
        ElectricMotor.__init__(self, battery_capacity, electric_range)
        self.fuel_efficiency = 35  # MPG
        self._drive_mode = "electric"  # "electric" or "gas"

    def set_drive_mode(self, mode: str) -> str:
        """Set drive mode."""
        if mode.lower() not in ["electric", "gas"]:
            raise ValueError("Mode must be 'electric' or 'gas'")
        self._drive_mode = mode.lower()
        return f"Drive mode set to {self._drive_mode}"

    def start_engine(self) -> str:
        """Start the hybrid car."""
        self._is_running = True
        if self._drive_mode == "electric":
            return ElectricMotor.start_motor(self)
        else:
            return Engine.start_engine(self)

    def stop_engine(self) -> str:
        """Stop the hybrid car."""
        result = ""
        if self._engine_running:
            result += Engine.stop_engine(self) + " "
        if self._motor_running:
            result += ElectricMotor.stop_motor(self)
        self._is_running = False
        return result.strip()

    def drive(self, miles: int) -> str:
        """Drive the hybrid car."""
        if not self._is_running:
            return "Cannot drive - vehicle is not running"

        if miles <= 0:
            raise ValueError("Miles must be positive")

        if self._drive_mode == "electric":
            return self._drive_electric(miles)
        else:
            return self._drive_gas(miles)

    def _drive_electric(self, miles: int) -> str:
        """Drive in electric mode."""
        energy_required = (miles / 100) * 15  # 15 kWh per 100 miles
        energy_available = (self._charge_level / 100) * self.battery_capacity

        if energy_required > energy_available:
            # Switch to gas mode automatically
            self._drive_mode = "gas"
            return f"Switched to gas mode. {self._drive_gas(miles)}"

        self._charge_level -= (energy_required / self.battery_capacity) * 100
        self._mileage += miles
        return f"Drove {miles} miles in electric mode. Energy used: {energy_required:.1f} kWh. Battery: {self._charge_level:.1f}%"

    def _drive_gas(self, miles: int) -> str:
        """Drive in gas mode."""
        self._mileage += miles
        fuel_used = miles / self.fuel_efficiency
        return f"Drove {miles} miles in gas mode. Fuel used: {fuel_used:.1f} gallons"

    def get_info(self) -> str:
        """Get hybrid car information."""
        info = Vehicle.get_info(self)
        info += f"\nDrive Mode: {self._drive_mode.capitalize()}"
        info += f"\nEngine: {self.engine_type} ({self.horsepower} HP)"
        info += f"\nBattery: {self.battery_capacity} kWh ({self.electric_range} miles electric range)"
        info += f"\n{self.get_battery_status()}"
        info += f"\nFuel Efficiency: {self.fuel_efficiency} MPG"
        return info


class Fleet:
    """Fleet management for vehicles."""

    def __init__(self, name: str):
        self.name = name
        self.vehicles: list[Vehicle] = []

    def add_vehicle(self, vehicle: Vehicle):
        """Add vehicle to fleet."""
        self.vehicles.append(vehicle)

    def get_total_mileage(self) -> int:
        """Get total mileage of all vehicles."""
        return sum(vehicle.mileage for vehicle in self.vehicles)

    def get_electric_vehicles(self) -> list[Vehicle]:
        """Get all electric vehicles."""
        return [v for v in self.vehicles if isinstance(v, ElectricMotor)]

    def get_gas_vehicles(self) -> list[Vehicle]:
        """Get all gas vehicles."""
        return [v for v in self.vehicles if isinstance(v, Engine) and not isinstance(v, ElectricMotor)]

    def service_due_vehicles(self, threshold: int = 10000) -> list[Vehicle]:
        """Get vehicles due for service."""
        return [v for v in self.vehicles if v.mileage % threshold == 0 and v.mileage > 0]

    def get_fleet_summary(self) -> str:
        """Get fleet summary."""
        total_vehicles = len(self.vehicles)
        total_mileage = self.get_total_mileage()
        electric_count = len(self.get_electric_vehicles())
        gas_count = len(self.get_gas_vehicles())

        summary = f"Fleet '{self.name}' Summary\n"
        summary += f"Total Vehicles: {total_vehicles}\n"
        summary += f"Total Mileage: {total_mileage}\n"
        summary += f"Electric Vehicles: {electric_count}\n"
        summary += f"Gas Vehicles: {gas_count}"

        if total_vehicles > 0:
            avg_mileage = total_mileage / total_vehicles
            summary += f"\nAverage Mileage: {avg_mileage:.1f}"

        return summary


# Demonstration
if __name__ == "__main__":
    print("=== Vehicle Hierarchy Demo ===\n")

    # Create vehicles
    gas_car = Car("Toyota", "Camry", 2020, "blue", "gasoline", 200)
    electric_car = ElectricCar("Tesla", "Model 3", 2021, "white", 75.0, 250)
    hybrid_car = HybridCar("Toyota", "Prius", 2022, "silver", "gasoline", 150, 12.0, 50)

    vehicles = [gas_car, electric_car, hybrid_car]

    print("Vehicle Information:")
    for vehicle in vehicles:
        print(f"\n{vehicle.get_info()}")

    print("\n" + "="*50)
    print("Vehicle Operations:")

    # Gas car operations
    print(f"\nGas Car: {gas_car.start_engine()}")
    print(f"{gas_car.drive(50)}")
    print(f"{gas_car.stop_engine()}")

    # Electric car operations
    print(f"\nElectric Car: {electric_car.start_engine()}")
    print(f"{electric_car.drive(100)}")
    print(f"{electric_car.charge_battery(2)}")
    print(f"{electric_car.stop_engine()}")

    # Hybrid car operations
    print(f"\nHybrid Car: {hybrid_car.set_drive_mode('electric')}")
    print(f"{hybrid_car.start_engine()}")
    print(f"{hybrid_car.drive(30)}")
    print(f"{hybrid_car.set_drive_mode('gas')}")
    print(f"{hybrid_car.drive(50)}")
    print(f"{hybrid_car.stop_engine()}")

    # Fleet management
    print("\n" + "="*50)
    print("Fleet Management:")

    fleet = Fleet("Company Fleet")
    for vehicle in vehicles:
        fleet.add_vehicle(vehicle)

    print(f"\n{fleet.get_fleet_summary()}")

    print(f"\nElectric vehicles: {len(fleet.get_electric_vehicles())}")
    print(f"Gas vehicles: {len(fleet.get_gas_vehicles())}")

    # Add more mileage for service check
    gas_car.mileage = 10000
    service_due = fleet.service_due_vehicles()
    if service_due:
        print(f"\nVehicles due for service: {[str(v) for v in service_due]}")

    print("\n=== OOP Concepts Demonstrated ===")
    print("- Multiple inheritance: HybridCar inherits from Vehicle, Engine, ElectricMotor")
    print("- Mixins: Engine and ElectricMotor as reusable components")
    print("- Abstract base class: Vehicle defines interface")
    print("- Method resolution order (MRO): Complex inheritance resolution")
    print("- Polymorphism: All vehicles implement drive() differently")
    print("- Composition: Fleet contains Vehicle objects")
    print("- isinstance() checks: Type-specific behavior")

    print("\n=== Multiple Inheritance Benefits ===")
    print("- Code reuse: Mixins provide specific functionality")
    print("- Flexible design: Combine features as needed")
    print("- Separation of concerns: Each mixin has single responsibility")
    print("- Avoid duplication: Common functionality in mixins")

    print("\n=== Method Resolution Order (MRO) ===")
    print("HybridCar MRO:", [cls.__name__ for cls in HybridCar.__mro__])
    print("This determines method call order in multiple inheritance")
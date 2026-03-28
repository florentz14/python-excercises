
"""
File Name: ITSE-1003/Examples/tv_class.py
Author: Florentino Báez
Date: 3/20/2026
Description: TV class example.
"""

class Tv:
    """Represents a TV with brand, model, and year."""
    
    def __init__(self, brand: str, model: str, year: int) -> None:
        """Initialize a new TV instance.
        
        Args:
            brand (str): The TV brand name
            model (str): The TV model name
            year (int): The manufacturing year
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.channel = 1
        self.volume = 50
    
    def turn_on(self) -> None:
        print(f"{self.brand} {self.model} is now ON")
    
    def turn_off(self) -> None:
        print(f"{self.brand} {self.model} is now OFF")
    
    def change_channel(self, channel: int) -> None:
        self.channel = channel
        print(f"Channel changed to {self.channel}")
    
    def adjust_volume(self, volume: int) -> None:
        self.volume = volume
        print(f"Volume adjusted to {self.volume}")
    
    def display_info(self) -> None:
        print(f"TV: {self.brand} {self.model} ({self.year})")
        print(f"Current channel: {self.channel}")
        print(f"Current volume: {self.volume}")

def main() -> None:
    """Main function to demonstrate the Tv class."""
    tv = Tv("Samsung", "QLED", 2023)
    tv.turn_on()
    tv.display_info()
    tv.change_channel(5)
    tv.adjust_volume(75)
    tv.display_info()
    tv.turn_off()

if __name__ == "__main__":
    main()
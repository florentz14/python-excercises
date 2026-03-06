"""
Simple conditional: Temperature advice
======================================
Topic: Conditionals (02_Conditionals)
Description: Give clothing advice based on temperature.
"""

temp = float(input("Enter temperature (°C): "))

if temp < 0:
    advice = "Wear heavy coat and gloves"
elif temp < 10:
    advice = "Wear a warm jacket"
elif temp < 20:
    advice = "A light sweater is enough"
elif temp < 30:
    advice = "T-shirt and shorts are fine"
else:
    advice = "Stay in the shade, drink water"

print(f"{temp}°C → {advice}")

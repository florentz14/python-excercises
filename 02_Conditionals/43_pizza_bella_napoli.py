# -------------------------------------------------
# File Name: 43_pizza_bella_napoli.py
# Description: Vegetarian or non-vegetarian pizza, choose ingredient
# -------------------------------------------------

VEG = ["Pepper", "Tofu"]
NON_VEG = ["Pepperoni", "Ham", "Salmon"]

choice = input("Vegetarian pizza? (y/n): ").strip().lower()
if choice == "y":
    options = VEG
else:
    options = NON_VEG

print("Choose one ingredient:")
for i, ing in enumerate(options, 1):
    print(f"  {i}. {ing}")
idx = int(input("Number: ")) - 1
ingredient = options[idx]

veg_str = "Vegetarian" if choice == "y" else "Non-vegetarian"
print(f"\n{veg_str} pizza:")
print("  Mozzarella, Tomato, " + ingredient)

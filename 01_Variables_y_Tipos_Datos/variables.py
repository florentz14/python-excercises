"""
Variables y tipos de datos básicos
===================================
Tema: Variables (01_Variables_y_Tipos_Datos)
Descripción: Variables enteras, operaciones, floats (precio e impuesto),
formateo de strings y f-strings para mostrar resultados.
"""
# Initialize integer variables
x = 3
y = 5
z = x + y  # Calculate the sum of x and y

# Calculate total price with tax
unit_price = 19.99  # Price of item in dollars
tax_rate = 0.07     # Tax rate as a decimal (7%)
total_price = unit_price * (1 + tax_rate)  # Apply tax to the unit price

# Display the sum of x and y
message = "The sum of x and y is: " + str(z)
print(message)

# Display the total price formatted to 2 decimal places
print(f"Total price after tax is: ${total_price:.2f}")
# -------------------------------------------------
# File Name: 11_filtrar.py
# Author: Florentino Báez
# Date: Pandas
# Description: Filter DataFrame Rows by Condition.
#              Use df[condition] to select rows that meet
#              a boolean condition. Combine conditions with
#              & (AND) and | (OR). Each condition must be
#              wrapped in parentheses.
# -------------------------------------------------

import pandas as pd

df = pd.DataFrame({
    "nombre": ["Ana", "Luis", "María", "Pedro"],
    "edad": [25, 30, 28, 35],
    "ciudad": ["Madrid", "Barcelona", "Valencia", "Madrid"],
})

# Filter: age >= 28
mayores = df[df["edad"] >= 28]
print("Edad >= 28:\n", mayores)

# Filter: city == "Madrid"
madrid = df[df["ciudad"] == "Madrid"]
print("\nCiudad Madrid:\n", madrid)

# Combined filter: (age >= 28) AND (city == "Madrid")
filtro = df[(df["edad"] >= 28) & (df["ciudad"] == "Madrid")]
print("\nEdad >= 28 y Madrid:\n", filtro)

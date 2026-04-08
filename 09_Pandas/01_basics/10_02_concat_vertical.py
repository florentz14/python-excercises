import pandas as pd


df_a = pd.DataFrame({"x": [1, 2]})
df_b = pd.DataFrame({"x": [3, 4]})

concat_v = pd.concat([df_a, df_b], ignore_index=True)

print("Concat vertical:")
print(concat_v)

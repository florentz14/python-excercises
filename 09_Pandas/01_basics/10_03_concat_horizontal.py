import pandas as pd


df_c = pd.DataFrame({"a": [1, 2]})
df_d = pd.DataFrame({"b": [10, 20]})

concat_h = pd.concat([df_c, df_d], axis=1)

print("Concat horizontal:")
print(concat_h)

import pandas as pd

from df_index_labels_data import data, labels


df = pd.DataFrame(data, index=labels)
df = df.iloc[2:]
df = df.reset_index()

print("DataFrame after reset_index():")
print(df)

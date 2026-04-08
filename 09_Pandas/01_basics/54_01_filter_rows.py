import pandas as pd

from df_index_labels_data import data, labels


df = pd.DataFrame(data, index=labels)
df = df.iloc[2:]

print("DataFrame after removing first two rows:")
print(df)

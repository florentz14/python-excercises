# Basic Pandas Use Cases

Quick reference for fundamental pandas operations. This folder contains Python scripts with runnable examples for each case.

---

## Scripts in this folder (basics/)

| Script | Case covered |
|--------|--------------|
| `01_create_dataframe.py` | Create DataFrame (dict, lists, Series, NumPy) |
| `02_read_csv.py` | Read and write CSV |
| `03_explore.py` | Explore data (head, tail, info, describe, value_counts) |
| `04_selection.py` | Selection (columns, loc, iloc, query) |
| `05_filter_sort.py` | Filter rows and sort (sort_values, nlargest) |
| `06_columns.py` | Create and modify columns (apply, map, rename) |
| `07_nulls.py` | Null values (isna, dropna, fillna) |
| `08_groupby.py` | Group and aggregate (groupby, agg) |
| `09_merge_concat.py` | Combine DataFrames (merge, concat) |
| `10_drop.py` | Drop columns, rows, duplicates |
| `11_statistics.py` | Basic statistics (mean, median, std, corr) |
| `12_time_series.py` | Time series (to_datetime, resample, pct_change) |

---

## 1. Create data structures

| Case | Description | Example | File |
|------|-------------|---------|------|
| Create DataFrame from dict | `pd.DataFrame(dict)` | Keys = columns, values = rows | `01_create_dataframe.py` |
| Create DataFrame from list | `pd.DataFrame(list_of_dicts)` | Each dict = one row | `01_create_dataframe.py` |
| Create Series | `pd.Series(list)` | 1D vector with index | `01_create_dataframe.py` |
| DataFrame from NumPy | `pd.DataFrame(arr)` | 2D array → DataFrame | `01_create_dataframe.py` |

---

## 2. Read and write files

| Case | Description | Example | File |
|------|-------------|---------|------|
| Read CSV | `pd.read_csv(path)` | Params: sep, encoding, index_col | `02_read_csv.py` |
| Read Excel | `pd.read_excel(path)` | Requires openpyxl | — |
| Export to CSV | `df.to_csv(path)` | Params: index=False, sep | `02_read_csv.py` |
| Export to Excel | `df.to_excel(path)` | Requires openpyxl | — |

---

## 3. Explore data

| Case | Description | Example | File |
|------|-------------|---------|------|
| First rows | `df.head(n)` | Default n=5 | `03_explore.py` |
| Last rows | `df.tail(n)` | Default n=5 | `03_explore.py` |
| Dimensions | `df.shape` | (rows, columns) | `03_explore.py` |
| Column info | `df.info()` | Types, nulls, memory | `03_explore.py` |
| Data types | `df.dtypes` | Type per column | `03_explore.py` |
| Statistics | `df.describe()` | count, mean, std, min, max, quartiles | `03_explore.py` |
| Unique values | `df['col'].unique()` | Array of distinct values | `03_explore.py` |
| Value counts | `df['col'].value_counts()` | Frequencies | `03_explore.py` |

---

## 4. Data selection

| Case | Description | Example | File |
|------|-------------|---------|------|
| Single column | `df['col']` or `df.col` | Returns Series | `04_selection.py` |
| Multiple columns | `df[['col1','col2']]` | Returns DataFrame | `04_selection.py` |
| By label (loc) | `df.loc[row, col]` | Name-based indexing | `04_selection.py` |
| By position (iloc) | `df.iloc[row, col]` | Integer indexing | `04_selection.py` |
| Filter rows | `df[df['col'] > value]` | Boolean indexing | `05_filter_sort.py` |
| Query | `df.query('col > value')` | String expression | `05_filter_sort.py` |

---

## 5. Filter and sort

| Case | Description | Example | File |
|------|-------------|---------|------|
| Filter by condition | `df[df['col'] == x]` | Comparisons, in, isin | `05_filter_sort.py` |
| Multiple conditions | `df[(cond1) & (cond2)]` | & (and), \| (or), ~ (not) | `05_filter_sort.py` |
| Sort by column | `df.sort_values('col')` | ascending, inplace | `05_filter_sort.py` |
| Sort by multiple | `df.sort_values(['c1','c2'])` | List of columns | `05_filter_sort.py` |
| Top N | `df.nlargest(n, 'col')` | First n by value | `05_filter_sort.py` |

---

## 6. Create and modify columns

| Case | Description | Example | File |
|------|-------------|---------|------|
| New column | `df['new'] = values` | Same length as df | `06_columns.py` |
| Computed column | `df['total'] = df['a'] + df['b']` | Operations between columns | `06_columns.py` |
| Apply function | `df['col'].apply(func)` | Per row | `06_columns.py` |
| Map values | `df['col'].map(dict)` | Replace by dictionary | `06_columns.py` |
| Rename columns | `df.rename(columns={'a':'b'})` | Old→new dict | `06_columns.py` |

---

## 7. Null values

| Case | Description | Example | File |
|------|-------------|---------|------|
| Detect nulls | `df.isna()` or `df.isnull()` | Boolean mask | `07_nulls.py` |
| Count nulls | `df['col'].isna().sum()` | Per column | `07_nulls.py` |
| Drop null rows | `df.dropna()` | subset, how, thresh | `07_nulls.py` |
| Fill nulls | `df.fillna(value)` | value, method='ffill' | `07_nulls.py` |

---

## 8. Group and aggregate

| Case | Description | Example | File |
|------|-------------|---------|------|
| Group by | `df.groupby('col')` | One or more columns | `08_groupby.py` |
| Mean per group | `df.groupby('col').mean()` | Or .sum(), .count(), .min(), .max() | `08_groupby.py` |
| Multiple aggregations | `df.groupby('col').agg(['mean','std'])` | agg with list or dict | `08_groupby.py` |
| Aggregation per column | `df.groupby('col').agg({'a':'mean','b':'sum'})` | Dict col→function | `08_groupby.py` |

---

## 9. Combine DataFrames

| Case | Description | Example | File |
|------|-------------|---------|------|
| Merge (join) | `pd.merge(df1, df2, on='col')` | inner, left, right, outer | `09_merge_concat.py` |
| Concat vertical | `pd.concat([df1, df2])` | axis=0, ignore_index | `09_merge_concat.py` |
| Concat horizontal | `pd.concat([df1, df2], axis=1)` | axis=1 | `09_merge_concat.py` |

---

## 10. Drop data

| Case | Description | Example | File |
|------|-------------|---------|------|
| Drop columns | `df.drop(columns=['col'])` | Or axis=1 | `10_drop.py` |
| Drop rows | `df.drop(index=[0,1])` | By label | `10_drop.py` |
| Drop duplicates | `df.drop_duplicates()` | subset, keep | `10_drop.py` |

---

## 11. Basic statistics

| Case | Description | Example | File |
|------|-------------|---------|------|
| Mean | `df['col'].mean()` | Per column | `11_statistics.py` |
| Median | `df['col'].median()` | — | `11_statistics.py` |
| Std deviation | `df['col'].std()` | — | `11_statistics.py` |
| Correlation | `df.corr()` | Correlation matrix | `11_statistics.py` |
| Quantiles | `df['col'].quantile(0.5)` | 0–1 | `11_statistics.py` |

---

## 12. Time series (basic)

| Case | Description | Example | File |
|------|-------------|---------|------|
| Date index | `pd.to_datetime(df['col'])` | DatetimeIndex | `12_time_series.py` |
| Resample | `df.resample('M').mean()` | M=monthly, D=daily | `12_time_series.py` |
| Percent change | `df['col'].pct_change()` | Variation between rows | `12_time_series.py` |

---

## Example files in parent folder (09_Pandas/)

Advanced examples in the parent directory. Basic cases are in this folder (basics/).

| File | Cases covered |
|------|---------------|
| `09_create_dataframe.py` | Create DataFrame |
| `10_read_csv.py` | Read CSV |
| `11_filter.py` | Filter rows |
| `12_columns.py` | Selection and column creation |
| `13_chipotle_explore.py` | Exploration (head, info, value_counts) |
| ... | See 09_Pandas/README.md for full list |

---

*Script path: `09_Pandas/` (one level above this folder)*

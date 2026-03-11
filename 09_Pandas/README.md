# 09_Pandas

Data analysis exercises with Pandas, organized by topic in subfolders.

**Requirements:** `pandas`, `numpy`; optional `matplotlib` (viz), `openpyxl` (Excel), `pyarrow` (Parquet).

**Run:** `python 01_basics/01_create_dataframe.py` (or any file) from `09_Pandas/`.

**Data path:** All CSV files in `09_Pandas/data/`. Scripts in subfolders use `Path(__file__).parent.parent / "data"`.

---

## Structure

```
09_Pandas/
├── 01_basics/           (30) Fundamentals, create, read, explore, dtypes
├── 02_selection_filtering/ (8)  loc/iloc, filter, sort, nlargest, sampling
├── 03_cleaning/         (13) Nulls, duplicates, outliers, string cleaning
├── 04_groupby_reshape/  (19) groupby, pivot, merge, crosstab
├── 05_time_series/      (11) Datetime, rolling, resample, forecasting
├── 06_real_world_projects/ (53) Full analyses by dataset
└── data/                All CSV files
```

---

## 01_basics (01-31)

| # | File | Description |
|---|------|-------------|
| 01 | `01_create_dataframe.py` | Create DataFrame from dict, lists, NumPy |
| 02 | `02_read_csv.py` | Read CSV, basic export |
| 03 | `03_explore.py` | head, tail, info, describe |
| 04 | `04_columns.py` | Select and create columns |
| 05 | `05_nulls.py` | isna, fillna, dropna |
| 06 | `06_merge_concat.py` | Merge and concat |
| 07 | `07_drop.py` | Drop rows, columns, duplicates |
| 08 | `08_statistics.py` | Basic statistics |
| 09 | `09_pokemon_series.py` | Series, DataFrame from dicts/lists |
| 10 | `10_index_operations.py` | set_index, reset_index |
| 11 | `11_value_counts.py` | Frequency counts and percentages |
| 12 | `12_astype_and_conversion.py` | Convert column data types safely |
| 13 | `13_to_numeric.py` | pd.to_numeric, errors=coerce |
| 14 | `14_series_from_list.py` | Create a Series from Python lists |
| 15 | `15_series_from_numpy.py` | Create a Series from NumPy arrays |
| 16 | `16_series_from_dictionary.py` | Create a Series from dictionaries |
| 17 | `17_series_custom_index.py` | Series with custom index labels |
| 18 | `18_series_named_attributes.py` | Series name and axis labels |
| 19 | `19_series_to_list.py` | Convert Series to Python list |
| 20 | `20_series_arithmetic.py` | Arithmetic operations between Series |
| 21 | `21_series_comparison.py` | Element-wise comparison operations |
| 22 | `22_dict_to_series.py` | Dictionary to Series conversion examples |
| 23 | `23_array_to_series.py` | NumPy array to Series conversion |
| 24 | `24_series_statistics.py` | Descriptive statistics for a Series |
| 25 | `25_series_word_length.py` | String length analysis with Series |

### New basics (26-30)

| # | File | Description |
|---|------|-------------|
| 26 | `26_merge_join_basics.py` | Merge by key, merge by index, and join with renamed columns |
| 27 | `27_concat_pivot_basics.py` | concat, combine_first, stack, and unstack |
| 28 | `28_mapping_replace_basics.py` | drop_duplicates, map dictionaries, replace values, rename index |
| 29 | `29_binning_outliers_sampling.py` | cut/qcut binning, outlier filtering, permutation sampling |
| 30 | `30_strings_and_advanced_groupby.py` | string cleanup, regex matching, groupby transform/apply |
| 31 | `31_merging_and_joining_in_depth.py` | full in-depth guide for merge/join variants and real-world example |

---

## 02_selection_filtering (01-08)

| # | File | Description |
|---|------|-------------|
| 01 | `01_selection.py` | loc, iloc |
| 02 | `02_filter_sort.py` | Filter by condition, sort_values |
| 03 | `03_chipotle_filter.py` | Boolean indexing, query, sort |
| 04 | `04_euro12_filter.py` | Filter teams by goals |
| 05 | `05_army_filter.py` | Complex conditions, top-N |
| 06 | `06_idxmax_idxmin.py` | Index of max/min values |
| 07 | `07_nlargest_nsmallest.py` | Top and bottom records |
| 08 | `08_sampling.py` | Random sampling (sample, frac) |

---

## 03_cleaning (01-13)

| # | File | Description |
|---|------|-------------|
| 01 | `01_string_methods.py` | str.lower, str.contains, str.replace |
| 02 | `02_categorical_binning.py` | pd.cut, pd.qcut |
| 03 | `03_data_cleaning.py` | Strip, replace, clip |
| 04 | `04_duplicate_detection.py` | duplicated(), drop_duplicates() |
| 05 | `05_outlier_detection.py` | IQR, z-score |
| 06 | `06_memory_optimization.py` | category dtype, memory_usage |
| 07 | `07_data_quality_report.py` | Automatic data quality checks |
| 08 | `08_duplicates.py` | Detect and remove duplicates |
| 09 | `09_elementwise_transform.py` | apply, map |
| 10 | `10_replace_values.py` | replace with scalars, dicts |
| 11 | `11_string_cleaning.py` | Clean text columns |
| 12 | `12_interpolate_general.py` | Fill missing with interpolation |
| 13 | `13_where_mask.py` | Conditional replacement |

---

## 04_groupby_reshape (01-19)

| # | File | Description |
|---|------|-------------|
| 01 | `01_groupby.py` | GroupBy basics |
| 02 | `02_alcohol_groupby.py` | groupby continent, agg |
| 03 | `03_occupation_groupby.py` | Mean age per occupation |
| 04 | `04_regiment_groupby.py` | Regiment/company scores |
| 05 | `05_auto_mpg_merge.py` | Inner/left/right/outer joins |
| 06 | `06_names_merge.py` | Multi-key merge |
| 07 | `07_house_merge.py` | 3-table merge |
| 08 | `08_pivot_melt.py` | pivot_table, melt, unstack |
| 09 | `09_multiindex.py` | MultiIndex, stack/unstack |
| 10 | `10_multiindex_groupby.py` | GroupBy with MultiIndex |
| 11 | `11_groupby_transform.py` | groupby + transform |
| 12 | `12_groupby_filter.py` | groupby + filter |
| 13 | `13_custom_aggregations.py` | Custom agg functions |
| 14 | `14_crosstab.py` | Cross-tabulation |
| 15 | `15_pivot_vs_pivot_table.py` | pivot_table with aggfunc |
| 16 | `16_explode.py` | Expand list-like columns |
| 17 | `17_json_normalize.py` | Flatten JSON into DataFrame |
| 18 | `18_rank.py` | Ranking values |
| 19 | `19_corr_cov.py` | Correlation and covariance |

---

## 05_time_series (01-11)

| # | File | Description |
|---|------|-------------|
| 01 | `01_time_series.py` | Time series basics |
| 02 | `02_wind_stats.py` | DatetimeIndex, resample, corr |
| 03 | `03_apple_stock_ts.py` | resample, rolling, pct_change |
| 04 | `04_financial_ts.py` | shift, moving averages |
| 05 | `05_investor_flow_ts.py` | Quarterly periods, cumsum |
| 06 | `06_rolling_window.py` | rolling mean, std |
| 07 | `07_expanding_window.py` | expanding statistics |
| 08 | `08_ewm_window.py` | Exponential weighted average |
| 09 | `09_time_series_features.py` | year, month, day, quarter |
| 10 | `10_time_series_resample_advanced.py` | Resample, ohlc |
| 11 | `11_time_series_forecasting_basics.py` | Rolling forecast |

---

## 06_real_world_projects (01-53)

Students (01-08), Chipotle/Occupation/Food (09-11), Apply (12-13), Stats (14), Viz (15-19), Delete (20-21), Sales/Attendance/Budget/Inventory/Tasks/Construction/Logs/Traffic/Movies/Transport (22-31), HR (32), Vectorization (33), Chunking (34), Export/Excel (35-36), API (37-38), Feature Engineering (39-41), Customer/Sales (42-43), Exercises (44-51), Sales Visualization Mini-Project (52), Sales Analysis Mini-Project (53). Menu launcher: `08_main_menu.py`.

---

## 07_unique_problems (01–81)

Unique Pandas practice exercises. Each file maps to one problem (e.g. `01_create_from_dict.py` -> problem 1). Covers: create from dict/list/numpy, index labels, selection, filtering, NaN handling, sort, rename, merge, groupby, time series, and more.

**Run:** `python 07_unique_problems/01_create_from_dict.py` (or any `NN_*.py`).

---

## Data Folder

All CSV files in `09_Pandas/data/`. Relational HR schema: `employees.csv`, `departments.csv`, `jobs.csv`, etc., plus dataset-specific files (titanic, chipotle, euro12, etc.).

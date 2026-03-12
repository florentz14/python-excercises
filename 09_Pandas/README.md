# 09_Pandas

Data analysis exercises with Pandas, organized by topic in subfolders.

**Requirements:** `pandas`, `numpy`; optional `matplotlib` (viz), `openpyxl` (Excel), `pyarrow` (Parquet).

**Run:** `python 01_basics/01_create_dataframe.py` (or any file) from `09_Pandas/`.

**Data path:** All CSV files in `09_Pandas/data/`. Scripts in subfolders use `Path(__file__).parent.parent / "data"`.

---

## Structure

```
09_Pandas/
├── 01_basics/           (74) Fundamentals, construction, indexing, and general ops
├── 02_selection_filtering/ (19) loc/iloc, masks, query, row/column selection
├── 03_sorting_sampling/ (10) sorting, top-N, sampling, shuffle/slicing windows
├── 04_cleaning/         (23) Nulls, replacements, dtype fixes, text cleaning
├── 05_groupby_reshape/  (24) groupby, pivot, merge, crosstab
├── 06_time_series/      (13) Datetime, rolling, resample, forecasting
├── 07_real_world_projects/ (55) Full analyses by dataset
└── data/                All CSV files
```

---

## 01_basics (01-31)

| # | File | Description |
|---|------|-------------|
| 01 | `01_create_dataframe.py` | Create DataFrame from dict, lists, NumPy |
| 02 | `04_read_csv.py` | Read CSV, basic export |
| 03 | `06_explore.py` | head, tail, info, describe |
| 04 | `07_columns.py` | Select and create columns |
| 05 | `09_nulls.py` | isna, fillna, dropna |
| 06 | `10_merge_concat.py` | Merge and concat |
| 07 | `11_drop.py` | Drop rows, columns, duplicates |
| 08 | `12_statistics.py` | Basic statistics |
| 09 | `13_pokemon_series.py` | Series, DataFrame from dicts/lists |
| 10 | `14_index_operations.py` | set_index, reset_index |
| 11 | `16_value_counts.py` | Frequency counts and percentages |
| 12 | `17_astype_and_conversion.py` | Convert column data types safely |
| 13 | `19_to_numeric.py` | pd.to_numeric, errors=coerce |
| 14 | `21_series_from_list.py` | Create a Series from Python lists |
| 15 | `23_series_from_numpy.py` | Create a Series from NumPy arrays |
| 16 | `24_series_from_dictionary.py` | Create a Series from dictionaries |
| 17 | `26_series_custom_index.py` | Series with custom index labels |
| 18 | `28_series_named_attributes.py` | Series name and axis labels |
| 19 | `30_series_to_list.py` | Convert Series to Python list |
| 20 | `32_series_arithmetic.py` | Arithmetic operations between Series |
| 21 | `34_series_comparison.py` | Element-wise comparison operations |
| 22 | `36_dict_to_series.py` | Dictionary to Series conversion examples |
| 23 | `37_array_to_series.py` | NumPy array to Series conversion |
| 24 | `39_series_statistics.py` | Descriptive statistics for a Series |
| 25 | `41_series_word_length.py` | String length analysis with Series |

### New basics (26-30)

| # | File | Description |
|---|------|-------------|
| 26 | `43_merge_join_basics.py` | Merge by key, merge by index, and join with renamed columns |
| 27 | `44_concat_pivot_basics.py` | concat, combine_first, stack, and unstack |
| 28 | `46_mapping_replace_basics.py` | drop_duplicates, map dictionaries, replace values, rename index |
| 29 | `47_binning_outliers_sampling.py` | cut/qcut binning, outlier filtering, permutation sampling |
| 30 | `48_strings_and_advanced_groupby.py` | string cleanup, regex matching, groupby transform/apply |
| 31 | `50_merging_and_joining_in_depth.py` | full in-depth guide for merge/join variants and real-world example |

---

## 02_selection_filtering (01-19)

| # | File | Description |
|---|------|-------------|
| 01 | `01_selection.py` | loc, iloc |
| 02 | `02_chipotle_filter.py` | Boolean indexing and filtering by condition |
| 03 | `03_euro12_filter.py` | Filter teams by goals |
| 04 | `04_army_filter.py` | Complex conditions for row filtering |
| 05 | `05_select_name_score.py` | Select specific columns from a DataFrame |
| 06 | `06_select_columns_rows.py` | Select columns and rows with labels |
| 07 | `07_rows_attempts_gt2.py` | Filter rows by numeric threshold |
| 08 | `08_count_rows_columns.py` | Quick shape and size checks |
| 09 | `09_score_between_15_20.py` | Range-based filtering |
| 10 | `10_change_score_row_d.py` | Update value using label selection |
| 11 | `11_select_rows_col1_eq4.py` | Filter with exact-value condition |
| 12 | `12_delete_rows_by_value.py` | Remove rows based on condition |
| 13 | `13_select_row_integer_index.py` | Integer-position row selection |
| 14 | `14_row_maximum_value.py` | Select rows by row-level maximum |
| 15 | `15_check_column_presence.py` | Validate column existence |
| 16 | `16_get_row_value.py` | Extract a single row/value |
| 17 | `17_select_all_except_one.py` | Select all columns except one |
| 18 | `18_select_columns_by_dtype.py` | Select columns by dtype |
| 19 | `19_local_variable_in_query.py` | Query with local Python variables |

---

## 03_sorting_sampling (01-10)

| # | File | Description |
|---|------|-------------|
| 01 | `01_filter_sort.py` | Filter and sort in one workflow |
| 02 | `02_idxmax_idxmin.py` | Index of max/min values |
| 03 | `03_nlargest_nsmallest.py` | Top and bottom records |
| 04 | `04_sampling.py` | Random sampling (`sample`, `frac`) |
| 05 | `05_shuffle_rows.py` | Shuffle rows randomly |
| 06 | `06_first_n_records.py` | First N records |
| 07 | `07_last_n_records.py` | Last N records |
| 08 | `08_remove_first_n_rows.py` | Drop first N rows |
| 09 | `09_remove_last_n_rows.py` | Drop last N rows |
| 10 | `10_split_random_subsets.py` | Split DataFrame into random subsets |

---

## 04_cleaning (01-23)

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
| 10 | `11_replace_values.py` | replace with scalars, dicts |
| 11 | `12_string_cleaning.py` | Clean text columns |
| 12 | `13_interpolate_general.py` | Fill missing with interpolation |
| 13 | `14_where_mask.py` | Conditional replacement |

---

## 05_groupby_reshape (01-24)

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

## 06_time_series (01-13)

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

## 07_real_world_projects (01-55)

Students (01-08), Chipotle/Occupation/Food (09-11), Apply (12-13), Stats (14), Viz (15-19), Delete (20-21), Sales/Attendance/Budget/Inventory/Tasks/Construction/Logs/Traffic/Movies/Transport (22-31), HR (32), Vectorization (33), Chunking (34), Export/Excel (35-36), API (37-38), Feature Engineering (39-41), Customer/Sales (42-43), Exercises (44-51), Sales Visualization Mini-Project (52), Sales Analysis Mini-Project (53), Books Catalog SQLite + Pandas (54), Books Catalog Analysis (55). Menu launcher: `08_main_menu.py`.

---

## Practice Exercises Distribution

The old `07_practice_problems` category was redistributed into the core topic folders so exercises live near the most relevant concepts:

- `01_basics`: 43 moved files
- `02_selection_filtering`: 21 moved files
- `04_cleaning`: 10 moved files
- `05_groupby_reshape`: 5 moved files
- `06_time_series`: 2 moved files

---

## Data Folder

All CSV files in `09_Pandas/data/`. Relational HR schema: `employees.csv`, `departments.csv`, `jobs.csv`, etc., plus dataset-specific files (titanic, chipotle, euro12, etc.).

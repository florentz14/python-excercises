# 09_Pandas

Data analysis exercises with Pandas, organized by topic in subfolders.

**Requirements:** `pandas`, `numpy`; optional `matplotlib` (viz), `openpyxl` (Excel), `pyarrow` (Parquet).

**Run:** `python 01_basics/04_read_csv.py` (or any existing file) from `09_Pandas/`.

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
├── 07_real_world_projects/ (63) Full analyses by dataset
└── data/                All CSV files
```

---

## 01_basics (01-74)

This folder now contains a mix of:
- **single-file lessons** (for short topics), and
- **modularized lessons** named with suffixes like `10_01_...`, `10_02_...`.

Examples of modularized groups:
- `07_01...07_04` (columns)
- `10_01...10_03` (merge/concat)
- `11_01...11_03` (drop operations)
- `12_01...12_04` (basic stats)
- `13_01...13_06` (pokemon series/dataframe/indexing)
- `14_01...14_04` (index operations)
- `30_01...30_05` (series to list)
- `32_01...32_04` (series arithmetic)
- `34_01...34_04` (series comparison)
- `39_01...39_04` (series stats)
- `41_01...41_04` (word length)
- `42_01...42_02`, `43_01...43_03`, `44_01...44_03`, `45_01...45_03`,
  `46_01...46_03`, `47_01...47_03`, `48_01...48_03`, `49_01...49_02`,
  `50_01...50_06`, `54_01...54_02`, `55_01...55_02`, `56_01...56_02`,
  `72_01...72_04`.

---

## 02_selection_filtering (01-19)

This folder is partially modularized:
- `01_selection.py` remains single-file.
- `02` to `13` are modularized as `NN_01...NN_0X` groups.
- `14` to `19` remain single-file lessons:
  - `14_row_maximum_value.py`
  - `15_check_column_presence.py`
  - `16_get_row_value.py`
  - `17_select_all_except_one.py`
  - `18_select_columns_by_dtype.py`
  - `19_local_variable_in_query.py`

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
| 01 | `01_01...01_04` | String cleanup, contains/extract, split/replace, length (modularized) |
| 02 | `02_categorical_binning.py` | pd.cut, pd.qcut |
| 03 | `03_data_cleaning.py` | Strip, replace, clip |
| 04 | `04_duplicate_detection.py` | duplicated(), drop_duplicates() |
| 05 | `05_outlier_detection.py` | IQR, z-score |
| 06 | `06_memory_optimization.py` | category dtype, memory_usage |
| 07 | `07_01...07_04` | Data quality overview, nulls/dupes, summaries, issue scan (modularized) |
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

## 07_real_world_projects (01-63)

Students (01-08), Chipotle/Occupation/Food (09-11), Apply (12-13), Stats (14), Viz (15-19), Delete (20-21), Sales/Attendance/Budget/Inventory/Tasks/Construction/Logs/Traffic/Movies/Transport (22-31), HR (32), Vectorization (33), Chunking (34), Export/Excel (35-36), API (37-38), Feature Engineering (39-41), Customer/Sales (42-43), Exercises (44-51), Sales Visualization Mini-Project (52), Sales Analysis Mini-Project (53), Books Catalog SQLite + Pandas (54), Books Catalog Analysis (55), Global Banks Regional Analysis (56), Global Banks Regional Visuals (57), Financial EDA Pipeline: Generator/Cleaning/Descriptive/Time-Series/Anomaly/Executive Report (58-63). Menu launcher: `08_main_menu.py`.

Detailed catalog for all scripts in this folder:
- `09_Pandas/07_real_world_projects/README.md`

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

All CSV files in `09_Pandas/data/`.

Key files used by current exercises:

- `exam_attempts.csv`: Extended student dataset for filtering/selection practice with columns:
  - `id`, `name`, `age`, `gender`, `score`, `attempts`, `qualify`, `grade`,
  - `study_hours_week`, `passed_mock_exam`, `region`, `enrollment_date`,
  - `attendance_pct`, `final_exam_score`, `absences`, `socioeconomic_tier`, `internet_access`.
- `data_dictionary.csv`: Column-level documentation (type, description, example, allowed range/values) for `exam_attempts.csv`.
- `exam_data.json`: JSON example dataset for import/parsing exercises.

Also includes dataset-specific files used across topics (for example `chipotle_orders.csv`, `euro12.csv`, and other project datasets).

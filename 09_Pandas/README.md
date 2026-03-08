# 09_Pandas

Data analysis exercises with Pandas, organized by level from basic to advanced.

**Requirements:** `pandas`, `numpy`; optional `matplotlib` (viz 37–41), `openpyxl` (Excel 80–81), `pyarrow` (Parquet 80).

**Run:** `python 01_create_dataframe.py` (or any `NN_*.py`) from `09_Pandas/`.

**Naming convention:** `NN_topic_action.py` — number, domain/dataset, operation (e.g. `21_chipotle_explore`, `32_auto_mpg_merge`).

---

## Fundamentals (01–12)

| File | Description |
|------|-------------|
| `01_create_dataframe.py` | Create a DataFrame from a dictionary |
| `02_read_csv.py` | Read a CSV file into a DataFrame |
| `03_explore.py` | Explore a DataFrame (head, tail, info, describe) |
| `04_selection.py` | Select rows and columns with loc/iloc |
| `05_filter_sort.py` | Filter rows by condition and sort |
| `06_columns.py` | Select and create columns |
| `07_nulls.py` | Handle null values (isna, fillna, dropna) |
| `08_groupby.py` | GroupBy operations |
| `09_merge_concat.py` | Merge and concat DataFrames |
| `10_drop.py` | Drop rows, columns, duplicates |
| `11_statistics.py` | Basic statistics |
| `12_time_series.py` | Time series basics |

## Students Performance Analysis (13–20)

| File | Description |
|------|-------------|
| `13_lunch_analysis.py` | Lunch type analysis (socioeconomic indicator) |
| `14_parental_education.py` | Parental education level analysis |
| `15_general_analysis.py` | General student performance analysis |
| `16_ethnic_group.py` | Ethnic group performance analysis |
| `17_gender_analysis.py` | Gender performance analysis |
| `18_test_preparation.py` | Test preparation impact analysis |
| `19_students_performance.py` | Full CSV analysis (load, stats, averages) |
| `20_main_menu.py` | Interactive menu to launch all analyses |

## Getting & Knowing (21–23)

| File | CSV | Description |
|------|-----|-------------|
| `21_chipotle_explore.py` | `chipotle_orders.csv` | Explore Chipotle orders: shape, info, dtypes, value_counts, revenue |
| `22_occupation_explore.py` | `occupation_users.csv` | Explore user demographics: unique occupations, describe, age stats |
| `23_food_facts.py` | `world_food_facts.csv` | Explore food nutrition: isnull, missing %, data quality |

## Filtering & Sorting (24–26)

| File | CSV | Description |
|------|-----|-------------|
| `24_chipotle_filter.py` | `chipotle_orders.csv` | Boolean indexing, query(), sort_values, loc/iloc |
| `25_euro12_filter.py` | `euro12.csv` | Filter teams by goals, sort, string filtering |
| `26_army_filter.py` | `fictional_army.csv` | Complex conditions, multi-sort, top-N selection |

## Grouping (27–29)

| File | CSV | Description |
|------|-----|-------------|
| `27_alcohol_groupby.py` | `alcohol_consumption.csv` | groupby continent, agg(mean/min/max/std), median |
| `28_occupation_groupby.py` | `grouping_occupation_users.csv` | Mean age per occupation, gender ratio, agg |
| `29_regiment_groupby.py` | `regiment.csv` | Regiment/company scores, improvement, multi-agg |

## Apply (30–31)

| File | CSV | Description |
|------|-----|-------------|
| `30_alcohol_apply.py` | `students_alcohol.csv` | apply, map, lambda, custom functions, risk flags |
| `31_crime_rates_apply.py` | `us_crime_rates.csv` | Per-capita rates, pct_change, normalization |

## Merge (32–34)

| File | CSV(s) | Description |
|------|--------|-------------|
| `32_auto_mpg_merge.py` | `auto_mpg_cars.csv`, `auto_mpg_origin.csv` | Inner/left/right/outer joins, suffixes |
| `33_names_merge.py` | `fictitious_personal.csv`, `fictitious_work.csv`, `fictitious_education.csv` | Multi-key merge, pd.concat, indicator |
| `34_house_merge.py` | `house_listings.csv`, `house_neighborhoods.csv`, `house_sales.csv` | 3-table merge, NaN detection, price analysis |

## Stats (35–36)

| File | CSV | Description |
|------|-----|-------------|
| `35_baby_names_stats.py` | `us_baby_names.csv` | rank, nunique, std, variance, trends |
| `36_wind_stats.py` | *(generated inline)* | DatetimeIndex, resample, corr, rolling avg, quantile |

## Visualization (37–41)

| File | CSV | Description |
|------|-----|-------------|
| `37_chipotle_viz.py` | `chipotle_viz.csv` | Bar, histogram, pie, horizontal bar charts |
| `38_titanic_viz.py` | `titanic.csv` | Survival charts, grouped bars, box plots |
| `39_scores_viz.py` | *(generated inline)* | Scatter, box, histogram, cumulative line |
| `40_retail_viz.py` | `online_retail.csv` | Sales trends, top products, country pie |
| `41_tips_viz.py` | *(generated inline)* | Scatter, box by day, tip percentage |

## Creating Series & DataFrames (42)

| File | CSV | Description |
|------|-----|-------------|
| `42_pokemon_series.py` | `pokemon.csv` | pd.Series, pd.DataFrame from dicts/lists/numpy, set_index |

## Time Series (43–45)

| File | CSV | Description |
|------|-----|-------------|
| `43_apple_stock_ts.py` | *(generated inline)* | DatetimeIndex, resample, rolling, pct_change |
| `44_financial_ts.py` | *(generated inline)* | shift, moving averages, drawdown, expanding |
| `45_investor_flow_ts.py` | *(generated inline)* | Quarterly periods, cumsum, trend analysis |

## Deleting (46–47)

| File | CSV | Description |
|------|-----|-------------|
| `46_iris_delete.py` | `iris.csv` | drop, dropna, del, pop, drop_duplicates |
| `47_wine_delete.py` | `wine_quality.csv` | Outlier removal, select_dtypes, fillna vs dropna |

## Real-World Analysis (48–57)

| File | CSV(s) | Description |
|------|--------|-------------|
| `48_sales_analysis.py` | `store_sales.csv` | Best product, best month, top customer |
| `49_student_attendance.py` | `student_attendance.csv` | Absences, attendance %, at-risk students |
| `50_personal_budget.py` | `personal_budget.csv` | Spending by category, monthly savings |
| `51_inventory.py` | `inventory_movements.csv`, `inventory_stock.csv` | Reorder, turnover, unsold products |
| `52_task_tracking.py` | `tasks.csv` | Pending by assignee, delays, completed |
| `53_construction.py` | `construction_materials.csv` | Consumption, waste, budget variance |
| `54_system_logs.py` | `system_logs.csv` | Most errors, peak hour, server warnings |
| `55_web_traffic.py` | `web_traffic.csv` | Top pages, traffic by day, conversion by source |
| `56_movies_analysis.py` | `movies.csv` | Best genre, releases by year, top 10 |
| `57_transport_analysis.py` | `transport.csv` | Longest route, trips by driver, delays |

## HR Database (58)

| File | CSV(s) | Description |
|------|--------|-------------|
| `58_hr_analysis.py` | `employees.csv`, `departments.csv`, `jobs.csv` | Headcount by dept, salary stats, top earners, hires by year |

## Reshape (59)

| File | Description |
|------|-------------|
| `59_pivot_melt.py` | pivot_table, melt, unstack — wide vs long format |

## String Methods (60)

| File | Description |
|------|-------------|
| `60_string_methods.py` | str.lower, str.contains, str.extract, str.split, str.replace |

## Categorical & Binning (61)

| File | Description |
|------|-------------|
| `61_categorical_binning.py` | categorical dtype, pd.cut, pd.qcut |

## Data Cleaning (62–64)

| File | Description |
|------|-------------|
| `62_data_cleaning.py` | Strip spaces, fix capitalization, replace values, clip |
| `63_duplicate_detection.py` | duplicated(), drop_duplicates() |
| `64_outlier_detection.py` | IQR and z-score outlier detection |

## Advanced Indexing (65–67)

| File | Description |
|------|-------------|
| `65_index_operations.py` | set_index, reset_index, rename index |
| `66_multiindex.py` | MultiIndex basics — hierarchical indexing, stack/unstack |
| `67_multiindex_groupby.py` | GroupBy with MultiIndex |

## Window Functions (68–70)

| File | Description |
|------|-------------|
| `68_rolling_window.py` | rolling mean, rolling std |
| `69_expanding_window.py` | expanding statistics |
| `70_ewm_window.py` | Exponential weighted moving average |

## Advanced GroupBy (71–73)

| File | Description |
|------|-------------|
| `71_groupby_transform.py` | groupby + transform |
| `72_groupby_filter.py` | groupby + filter |
| `73_custom_aggregations.py` | Custom aggregation functions |

## Performance (74–76)

| File | Description |
|------|-------------|
| `74_vectorization.py` | Vectorized operations vs loops |
| `75_memory_optimization.py` | category dtype, memory_usage |
| `76_chunk_processing.py` | read_csv chunksize for big data |

## Advanced Time Series (77–79)

| File | Description |
|------|-------------|
| `77_time_series_features.py` | Extract year, month, day, quarter |
| `78_time_series_resample_advanced.py` | Advanced resampling, ohlc |
| `79_time_series_forecasting_basics.py` | Rolling forecast, naive, pct_change |

## Export (80–81)

| File | Description |
|------|-------------|
| `80_export_files.py` | to_csv, to_json, to_excel, to_parquet |
| `81_excel_operations.py` | Multiple sheets, read_excel |

## API Data (82–83)

| File | Description |
|------|-------------|
| `82_api_data_loading.py` | Load JSON from API, pd.DataFrame |
| `83_api_to_dataframe.py` | pd.json_normalize, nested JSON |

## Feature Engineering (84–86)

| File | Description |
|------|-------------|
| `84_feature_engineering.py` | Derived features, lag, diff |
| `85_encoding_features.py` | One-hot, get_dummies, label encoding |
| `86_scaling_features.py` | Min-max, z-score, robust scale |

## Data Projects (87–89)

| File | CSV | Description |
|------|-----|-------------|
| `87_customer_segmentation.py` | `store_sales.csv` | RFM analysis |
| `88_sales_forecast_project.py` | `store_sales.csv` | Sales forecasting with rolling |
| `89_data_quality_report.py` | `store_sales.csv` | Automatic data quality checks |

## Pandas Exercises (90–97)

| File | CSV(s) | Description |
|------|--------|-------------|
| `90_sales_discount.py` | — | Sales by year with 10% discount |
| `91_grades_stats.py` | — | Grade statistics: min, max, mean, std |
| `92_grades_passed.py` | — | Passing grades sorted descending |
| `93_sales_dataframe.py` | — | DataFrame Month, Sales, Expenses |
| `94_balance_months.py` | — | Balance total for given months |
| `95_stock_quotes.py` | `cotizacion.csv` | IBEX35 quotes: min, max, mean |
| `96_titanic_analysis.py` | `titanic.csv` | Full Titanic analysis |
| `97_emissions_analysis.py` | `emisiones-2016/17/18/19.csv` | Madrid emissions, reshape, summaries |

---

## Data Folder

All CSV files are located in `09_Pandas/data/`. Python scripts reference them via `Path(__file__).parent / "data" / "filename.csv"`.

## HR Database CSVs (in data/)

Relational dataset based on the classic HR schema (employees, departments, jobs).

| CSV | Rows | Description |
|-----|------|-------------|
| `employees.csv` | 120 | Employee records (id, name, email, phone, hire date, job, salary, manager, department) |
| `departments.csv` | 32 | Departments with manager and location references |
| `jobs.csv` | 25 | Job titles with min/max salary ranges |
| `job_history.csv` | 20 | Employee career transitions with dates |
| `countries.csv` | 55 | Countries grouped by region |
| `regions.csv` | 5 | Geographic regions (Europe, Americas, Asia, Middle East & Africa, Oceania) |
| `locations.csv` | 30 | Office locations worldwide |
| `players.csv` | 40 | Player stats: team, position, age, score, goals, attempts, qualified |

# 09_Pandas

Data analysis exercises with Pandas, organized by topic.

---

## Students Performance Analysis (01–08)

| File | Description |
|------|-------------|
| `01_analisis_almuerzo.py` | Lunch type analysis (socioeconomic indicator) |
| `02_analisis_educacion_parental.py` | Parental education level analysis |
| `03_analisis_general.py` | General student performance analysis |
| `04_analisis_grupo_etnico.py` | Ethnic group performance analysis |
| `05_analisis_por_genero.py` | Gender performance analysis |
| `06_analisis_preparacion.py` | Test preparation impact analysis |
| `07_analisis_students_performance.py` | Full CSV analysis (load, stats, averages) |
| `08_menu_principal.py` | Interactive menu to launch all analyses |

## Pandas Basics (09–12)

| File | Description |
|------|-------------|
| `09_crear_dataframe.py` | Create a DataFrame from a dictionary |
| `10_leer_csv.py` | Read a CSV file into a DataFrame |
| `11_filtrar.py` | Filter rows by condition |
| `12_columnas.py` | Select and create columns |

## Getting & Knowing (13–15)

| File | CSV | Description |
|------|-----|-------------|
| `13_chipotle_explore.py` | `chipotle_orders.csv` | Explore Chipotle orders: shape, info, dtypes, value_counts, revenue |
| `14_occupation_explore.py` | `occupation_users.csv` | Explore user demographics: unique occupations, describe, age stats |
| `15_food_facts_explore.py` | `world_food_facts.csv` | Explore food nutrition: isnull, missing %, data quality |

## Filtering & Sorting (16–18)

| File | CSV | Description |
|------|-----|-------------|
| `16_chipotle_filter.py` | `chipotle_orders.csv` | Boolean indexing, query(), sort_values, loc/iloc |
| `17_euro12_filter.py` | `euro12.csv` | Filter teams by goals, sort, string filtering |
| `18_army_filter.py` | `fictional_army.csv` | Complex conditions, multi-sort, top-N selection |

## Grouping (19–21)

| File | CSV | Description |
|------|-----|-------------|
| `19_alcohol_groupby.py` | `alcohol_consumption.csv` | groupby continent, agg(mean/min/max/std), median |
| `20_occupation_groupby.py` | `grouping_occupation_users.csv` | Mean age per occupation, gender ratio, agg |
| `21_regiment_groupby.py` | `regiment.csv` | Regiment/company scores, improvement, multi-agg |

## Apply (22–23)

| File | CSV | Description |
|------|-----|-------------|
| `22_alcohol_apply.py` | `students_alcohol.csv` | apply, map, lambda, custom functions, risk flags |
| `23_crime_rates_apply.py` | `us_crime_rates.csv` | Per-capita rates, pct_change, normalization |

## Merge (24–26)

| File | CSV(s) | Description |
|------|--------|-------------|
| `24_auto_mpg_merge.py` | `auto_mpg_cars.csv`, `auto_mpg_origin.csv` | Inner/left/right/outer joins, suffixes |
| `25_names_merge.py` | `fictitious_personal.csv`, `fictitious_work.csv`, `fictitious_education.csv` | Multi-key merge, pd.concat, indicator |
| `26_house_merge.py` | `house_listings.csv`, `house_neighborhoods.csv`, `house_sales.csv` | 3-table merge, NaN detection, price analysis |

## Stats (27–28)

| File | CSV | Description |
|------|-----|-------------|
| `27_baby_names_stats.py` | `us_baby_names.csv` | rank, nunique, std, variance, trends |
| `28_wind_stats.py` | *(generated inline)* | DatetimeIndex, resample, corr, rolling avg, quantile |

## Visualization (29–33)

| File | CSV | Description |
|------|-----|-------------|
| `29_chipotle_viz.py` | `chipotle_viz.csv` | Bar, histogram, pie, horizontal bar charts |
| `30_titanic_viz.py` | `titanic.csv` | Survival charts, grouped bars, box plots |
| `31_scores_viz.py` | *(generated inline)* | Scatter, box, histogram, cumulative line |
| `32_retail_viz.py` | `online_retail.csv` | Sales trends, top products, country pie |
| `33_tips_viz.py` | *(generated inline)* | Scatter, box by day, tip percentage |

## Creating Series & DataFrames (34)

| File | CSV | Description |
|------|-----|-------------|
| `34_pokemon_series.py` | `pokemon.csv` | pd.Series, pd.DataFrame from dicts/lists/numpy, set_index |

## Time Series (35–37)

| File | CSV | Description |
|------|-----|-------------|
| `35_apple_stock_ts.py` | *(generated inline)* | DatetimeIndex, resample, rolling, pct_change |
| `36_financial_ts.py` | *(generated inline)* | shift, moving averages, drawdown, expanding |
| `37_investor_flow_ts.py` | *(generated inline)* | Quarterly periods, cumsum, trend analysis |

## Deleting (38–39)

| File | CSV | Description |
|------|-----|-------------|
| `38_iris_delete.py` | `iris.csv` | drop, dropna, del, pop, drop_duplicates |
| `39_wine_delete.py` | `wine_quality.csv` | Outlier removal, select_dtypes, fillna vs dropna |

---

## HR Database CSVs

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

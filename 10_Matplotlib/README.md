# 10_Matplotlib

Data visualization with Matplotlib (and Seaborn).

## Core Concepts (files 01-14)

These files teach fundamental chart types and Matplotlib features using inline data.

| File | Topic | Key Concepts |
|------|-------|--------------|
| `01_pyplot_intro.py` | Pyplot Introduction | `plt.plot()`, `plt.show()`, `plt.savefig()`, OOP vs pyplot |
| `02_plotting.py` | Plotting Data Points | Format strings, keyword args, plotting from dicts |
| `03_markers.py` | Markers | Marker types, size, face/edge color, `markevery` |
| `04_line.py` | Line Styles | Solid, dashed, dotted, line width, colors, `fill_between` |
| `05_labels.py` | Labels & Annotations | Titles, axis labels, legend, `annotate()`, tick labels |
| `06_grid.py` | Grid Lines | Axis grid, style, major/minor grids, background color |
| `07_subplot.py` | Subplots | `subplot()`, `subplots()`, GridSpec, shared axes |
| `08_scatter.py` | Scatter Plots | Colors, colormaps, trend lines, bubble sizes |
| `09_bars.py` | Bar Charts | Vertical, horizontal, grouped, stacked, error bars |
| `10_histograms.py` | Histograms | Bins, density, overlapping, cumulative, step |
| `11_pie_charts.py` | Pie Charts | Percentages, explode, donut, nested pie |
| `12_boxplot.py` | Box Plots | Median, quartiles, outliers, `patch_artist` |
| `13_estadistico_multi.py` | Multi-Chart Stats | Side-by-side histogram + boxplot |
| `14_pandas_seaborn.py` | Pandas + Seaborn | `sns.lineplot`, `barplot`, `boxplot`, `histplot` |

---

## Applied Charts with CSV Data (files 15-53)

Each file creates **one chart** using CSV datasets from the `09_Pandas/` folder.

### Employees (`employees.csv` + `departments.csv`)

| File | Chart Type | Description |
|------|-----------|-------------|
| `15_employees_avg_salary.py` | Horizontal bar | Top 10 departments by average salary |
| `16_employees_salary_hist.py` | Histogram | Salary distribution with mean & median lines |
| `17_employees_dept_pie.py` | Pie chart | Employee distribution by department |
| `18_employees_salary_box.py` | Box plot | Salary distribution by department (top 6) |

### Players (`players.csv`)

| File | Chart Type | Description |
|------|-----------|-------------|
| `19_players_goals_scatter.py` | Scatter | Goals vs score colored by position |
| `20_players_top_scorers.py` | Horizontal bar | Top 10 players by score |
| `21_players_team_bar.py` | Grouped bar | Average goals vs attempts by team |
| `22_players_position_pie.py` | Pie chart | Player distribution by position |

### Iris (`iris.csv`)

| File | Chart Type | Description |
|------|-----------|-------------|
| `23_iris_sepal_scatter.py` | Scatter | Sepal length vs width by species |
| `24_iris_petal_scatter.py` | Scatter | Petal length vs width by species |
| `25_iris_feature_hist.py` | Histogram (2x2) | Feature distributions by species |
| `26_iris_feature_box.py` | Box plot (1x4) | All features by species side by side |

### Pokémon (`pokemon.csv`)

| File | Chart Type | Description |
|------|-----------|-------------|
| `27_pokemon_radar.py` | Radar/Spider | Compare stats of 4 selected Pokémon |
| `28_pokemon_total_stats.py` | Horizontal bar | Total stats per Pokémon (sorted) |
| `29_pokemon_attack_defense.py` | Grouped bar | Attack vs defense per Pokémon |

### Wine Quality (`wine_quality.csv`)

| File | Chart Type | Description |
|------|-----------|-------------|
| `30_wine_alcohol_hist.py` | Histogram | Alcohol distribution red vs white |
| `31_wine_type_box.py` | Box plot | Alcohol and pH by wine type |
| `32_wine_quality_scatter.py` | Scatter | Alcohol vs quality rating with jitter |
| `33_wine_quality_bar.py` | Grouped bar | Avg properties by quality rating |

### Alcohol Consumption (`alcohol_consumption.csv`)

| File | Chart Type | Description |
|------|-----------|-------------|
| `34_alcohol_total_bar.py` | Horizontal bar | Total litres by country |
| `35_alcohol_stacked_bar.py` | Stacked bar | Beer, spirits, wine per country |
| `36_alcohol_continent_pie.py` | Pie chart | Average consumption by continent |
| `37_alcohol_top8_bar.py` | Grouped bar | Beer vs wine vs spirits (top 8) |

### US Crime Rates (`us_crime_rates.csv`)

| File | Chart Type | Description |
|------|-----------|-------------|
| `38_crime_trend_line.py` | Line chart | Violent vs property crime over time |
| `39_crime_area_chart.py` | Stacked area | Murder, robbery, burglary over time |
| `40_crime_type_panels.py` | Subplots (2x2) | Individual crime type trends |
| `41_crime_murder_bar.py` | Bar + trend | Murder count per year with quadratic fit |

### Students & Alcohol (`students_alcohol.csv`)

| File | Chart Type | Description |
|------|-----------|-------------|
| `42_students_grade_hist.py` | Histogram | Final grade distribution with mean line |
| `43_students_study_scatter.py` | Scatter | Study time vs final grade by sex |
| `44_students_school_box.py` | Box plot (1x3) | G1, G2, G3 grades by school |
| `45_students_alcohol_bar.py` | Bar chart | Avg final grade by weekend alcohol level |

### Euro 2012 (`euro12.csv`)

| File | Chart Type | Description |
|------|-----------|-------------|
| `46_euro12_goals_bar.py` | Horizontal bar | Goals scored by team |
| `47_euro12_shots_bar.py` | Grouped bar | Shots on vs off target |
| `48_euro12_accuracy_scatter.py` | Scatter | Accuracy vs goals (color = passes) |
| `49_euro12_radar.py` | Radar/Spider | Top 3 teams comparison (normalized) |

### Auto MPG (`auto_mpg_cars.csv`)

| File | Chart Type | Description |
|------|-----------|-------------|
| `50_auto_hp_scatter.py` | Scatter | Horsepower vs MPG by cylinders + trend |
| `51_auto_mpg_hist.py` | Histogram (1x3) | MPG distribution per cylinder count |
| `52_auto_mpg_bar.py` | Bar chart | Average MPG by cylinder count |
| `53_auto_bubble_chart.py` | Bubble chart | Displacement vs MPG (size = HP) |

---

## Chart Types Index

| Chart Type | Files |
|------------|-------|
| Line plot | 01, 02, 04, 14, 38 |
| Scatter plot | 08, 19, 23, 24, 32, 43, 48, 50 |
| Bar (horizontal) | 09, 15, 20, 28, 34, 46 |
| Bar (vertical) | 09, 41, 45, 52 |
| Grouped bar | 09, 21, 29, 33, 37, 47 |
| Stacked bar | 09, 35, 39 |
| Histogram | 10, 16, 25, 30, 42, 51 |
| Pie / Donut | 11, 17, 22, 36 |
| Box plot | 12, 13, 18, 26, 31, 44 |
| Radar / Spider | 27, 49 |
| Area chart | 04, 39, 40 |
| Bubble chart | 53 |
| Trend line | 08, 41, 50 |

## Requirements

```
matplotlib
numpy
pandas
seaborn    # only for 14_pandas_seaborn.py
scipy      # only for 10_histograms.py (norm.pdf)
```

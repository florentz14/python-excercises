# 10_Matplotlib

Data visualization with Matplotlib (and Seaborn). Each file contains **one chart**.

## 01-04 — Pyplot Introduction

| File | Chart |
|------|-------|
| `01_pyplot_basic_plot.py` | Basic plot: Y-only vs X+Y (2 subplots) |
| `02_pyplot_multiple_lines.py` | Multiple lines on one plot (x², x³) |
| `03_pyplot_save_figure.py` | Saving a figure to file demo |
| `04_pyplot_oop_style.py` | Object-oriented approach (fig, ax) |

## 05-09 — Plotting Data Points

| File | Chart |
|------|-------|
| `05_plotting_two_points.py` | Line between two points |
| `06_plotting_markers_only.py` | Points only, no connecting line |
| `07_plotting_multiple_styles.py` | Multiple lines with format strings |
| `08_plotting_keyword_args.py` | Plot with keyword arguments |
| `09_plotting_from_dict.py` | Plotting from a dictionary |

## 10-15 — Markers

| File | Chart |
|------|-------|
| `10_markers_basic.py` | Default circle marker |
| `11_markers_types.py` | Different marker types (2x3 grid) |
| `12_markers_sizes.py` | Different marker sizes |
| `13_markers_colors.py` | Face color, edge color, hollow (3 subplots) |
| `14_markers_format_string.py` | Format string shortcuts with markers |
| `15_markers_every_nth.py` | markevery — show every Nth point |

## 16-20 — Line Styles

| File | Chart |
|------|-------|
| `16_line_styles.py` | Solid, dashed, dashdot, dotted (2x2 grid) |
| `17_line_width.py` | Different line widths |
| `18_line_colors.py` | Named, hex, and RGB colors |
| `19_line_multiple_styled.py` | Multiple styled lines (sin, cos, sin*cos) |
| `20_line_fill_between.py` | Lines with fill_between and alpha |

## 21-26 — Labels, Titles, and Annotations

| File | Chart |
|------|-------|
| `21_labels_basic.py` | Basic title, xlabel, ylabel |
| `22_labels_custom_font.py` | Custom font size, weight, family, color |
| `23_labels_title_position.py` | Title alignment: left, center, right |
| `24_labels_legend.py` | Legend with position and style control |
| `25_labels_annotations.py` | Text annotations with arrows |
| `26_labels_tick_custom.py` | Custom tick labels (month names) |

## 27-32 — Grid Lines

| File | Chart |
|------|-------|
| `27_grid_basic.py` | Basic grid on/off |
| `28_grid_axis.py` | Grid on specific axis (both, x, y) |
| `29_grid_custom_style.py` | Grid color, linestyle, linewidth, alpha |
| `30_grid_line_styles.py` | Different grid line styles (2x2 grid) |
| `31_grid_major_minor.py` | Major and minor grid lines |
| `32_grid_colored_bg.py` | Grid with colored background |

## 33-37 — Subplots

| File | Chart |
|------|-------|
| `33_subplot_side_by_side.py` | Two subplots side by side (1x2) |
| `34_subplot_stacked.py` | Stacked subplots (2x1) |
| `35_subplot_grid.py` | 2x3 grid of trig functions |
| `36_subplot_mixed_layout.py` | Mixed layout with GridSpec |
| `37_subplot_shared_axes.py` | Shared Y-axis between subplots |

## 38-43 — Scatter Plots

| File | Chart |
|------|-------|
| `38_scatter_basic.py` | Basic scatter (age vs speed) |
| `39_scatter_two_datasets.py` | Compare two datasets |
| `40_scatter_colormap.py` | Colormap with varying sizes |
| `41_scatter_colormaps.py` | Different colormaps comparison (2x2) |
| `42_scatter_alpha.py` | Transparency with 500 points |
| `43_scatter_trend_line.py` | Student grades with polyfit trend |

## 44-50 — Bar Charts

| File | Chart |
|------|-------|
| `44_bars_basic.py` | Basic vertical bar chart |
| `45_bars_horizontal.py` | Horizontal bar chart (barh) |
| `46_bars_custom_colors.py` | Custom colors with value labels |
| `47_bars_width.py` | Thin vs wide bars (2 subplots) |
| `48_bars_grouped.py` | Grouped bar chart (3 products) |
| `49_bars_stacked.py` | Stacked bar chart |
| `50_bars_error.py` | Bar chart with error bars |

## 51-57 — Histograms

| File | Chart |
|------|-------|
| `51_hist_basic.py` | Basic histogram (15 bins) |
| `52_hist_bins.py` | Different bin counts (5, 15, 50) |
| `53_hist_density.py` | Density histogram with normal curve |
| `54_hist_overlapping.py` | Two overlapping histograms |
| `55_hist_horizontal.py` | Horizontal histogram |
| `56_hist_cumulative.py` | Cumulative histogram |
| `57_hist_step.py` | Step histogram (outline + filled) |

## 58-64 — Pie Charts

| File | Chart |
|------|-------|
| `58_pie_basic.py` | Basic pie chart |
| `59_pie_percentages.py` | Pie with percentages (autopct) |
| `60_pie_customized.py` | Custom colors, explode, shadow |
| `61_pie_legend.py` | Pie with external legend |
| `62_pie_donut.py` | Donut chart (center hole) |
| `63_pie_exploded.py` | All slices slightly exploded |
| `64_pie_nested.py` | Nested pie (outer + inner ring) |

## 65-67 — Additional Concepts

| File | Chart |
|------|-------|
| `65_boxplot.py` | Box plot (median, quartiles, outliers) |
| `66_statistical_multi.py` | Histogram + boxplot side by side |
| `67_pandas_seaborn.py` | Pandas + Matplotlib + Seaborn (2x2 dashboard) |

---

## Applied Charts with CSV Data (files 68-109)

Each file creates one chart using CSV datasets from the `09_Pandas/` folder.

### Employees (`employees.csv` + `departments.csv`)

| File | Chart Type |
|------|-----------|
| `68_employees_avg_salary.py` | Horizontal bar — avg salary by dept |
| `69_employees_salary_hist.py` | Histogram — salary distribution |
| `70_employees_dept_pie.py` | Pie — employee distribution by dept |
| `71_employees_salary_box.py` | Box plot — salary by department |

### Players (`players.csv`)

| File | Chart Type |
|------|-----------|
| `72_players_goals_scatter.py` | Scatter — goals vs score by position |
| `73_players_top_scorers.py` | Horizontal bar — top 10 by score |
| `74_players_team_bar.py` | Grouped bar — goals vs attempts by team |
| `75_players_position_pie.py` | Pie — player distribution by position |

### Iris (`iris.csv`)

| File | Chart Type |
|------|-----------|
| `76_iris_sepal_scatter.py` | Scatter — sepal dimensions by species |
| `77_iris_petal_scatter.py` | Scatter — petal dimensions by species |
| `78_iris_feature_hist.py` | Histogram (2x2) — feature distributions |
| `79_iris_feature_box.py` | Box plot (1x4) — features by species |

### Pokémon (`pokemon.csv`)

| File | Chart Type |
|------|-----------|
| `80_pokemon_radar.py` | Radar — compare 4 Pokémon stats |
| `81_pokemon_total_stats.py` | Horizontal bar — total stats sorted |
| `82_pokemon_attack_defense.py` | Grouped bar — attack vs defense |

### Wine Quality (`wine_quality.csv`)

| File | Chart Type |
|------|-----------|
| `83_wine_alcohol_hist.py` | Histogram — alcohol by wine type |
| `84_wine_type_box.py` | Box plot — alcohol and pH by type |
| `85_wine_quality_scatter.py` | Scatter — alcohol vs quality |
| `86_wine_quality_bar.py` | Grouped bar — properties by quality |

### Alcohol Consumption (`alcohol_consumption.csv`)

| File | Chart Type |
|------|-----------|
| `87_alcohol_total_bar.py` | Horizontal bar — total litres by country |
| `88_alcohol_stacked_bar.py` | Stacked bar — beer/spirits/wine |
| `89_alcohol_continent_pie.py` | Pie — avg consumption by continent |
| `90_alcohol_top8_bar.py` | Grouped bar — top 8 countries |

### US Crime Rates (`us_crime_rates.csv`)

| File | Chart Type |
|------|-----------|
| `91_crime_trend_line.py` | Line — violent vs property over time |
| `92_crime_area_chart.py` | Stacked area — crime categories |
| `93_crime_type_panels.py` | Subplots (2x2) — individual crime trends |
| `94_crime_murder_bar.py` | Bar + trend — murder per year |

### Students & Alcohol (`students_alcohol.csv`)

| File | Chart Type |
|------|-----------|
| `95_students_grade_hist.py` | Histogram — final grade distribution |
| `96_students_study_scatter.py` | Scatter — study time vs grade |
| `97_students_school_box.py` | Box plot — grades by school |
| `98_students_alcohol_bar.py` | Bar — grade vs alcohol level |

### Euro 2012 (`euro12.csv`)

| File | Chart Type |
|------|-----------|
| `99_euro12_goals_bar.py` | Horizontal bar — goals by team |
| `100_euro12_shots_bar.py` | Grouped bar — shots on/off target |
| `101_euro12_accuracy_scatter.py` | Scatter — accuracy vs goals |
| `102_euro12_radar.py` | Radar — top 3 teams normalized |

### Auto MPG (`auto_mpg_cars.csv`)

| File | Chart Type |
|------|-----------|
| `103_auto_hp_scatter.py` | Scatter — HP vs MPG by cylinders |
| `104_auto_mpg_hist.py` | Histogram (1x3) — MPG per cylinder |
| `105_auto_mpg_bar.py` | Bar — avg MPG by cylinder count |
| `106_auto_bubble_chart.py` | Bubble — displacement vs MPG |

### Additional Examples

| File | Chart Type |
|------|-----------|
| `107_turtle_shapes_circle_triangle_square.py` | Turtle shapes |
| `108_sine_wave.py` | Sine wave |
| `109_math_functions_quadratic_exponential.py` | Math functions (quadratic, exponential) |

---

## Requirements

```
matplotlib
numpy
pandas
seaborn    # only for 67_pandas_seaborn.py
scipy      # only for 53_hist_density.py
```

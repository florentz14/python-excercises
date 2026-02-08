# 10_Matplotlib

Data visualization with Matplotlib (and Seaborn). Each file contains **one chart**.

## 01 — Pyplot Introduction

| File | Chart |
|------|-------|
| `01a_pyplot_basic_plot.py` | Basic plot: Y-only vs X+Y (2 subplots) |
| `01b_pyplot_multiple_lines.py` | Multiple lines on one plot (x², x³) |
| `01c_pyplot_save_figure.py` | Saving a figure to file demo |
| `01d_pyplot_oop_style.py` | Object-oriented approach (fig, ax) |

## 02 — Plotting Data Points

| File | Chart |
|------|-------|
| `02a_plotting_two_points.py` | Line between two points |
| `02b_plotting_markers_only.py` | Points only, no connecting line |
| `02c_plotting_multiple_styles.py` | Multiple lines with format strings |
| `02d_plotting_keyword_args.py` | Plot with keyword arguments |
| `02e_plotting_from_dict.py` | Plotting from a dictionary |

## 03 — Markers

| File | Chart |
|------|-------|
| `03a_markers_basic.py` | Default circle marker |
| `03b_markers_types.py` | Different marker types (2x3 grid) |
| `03c_markers_sizes.py` | Different marker sizes |
| `03d_markers_colors.py` | Face color, edge color, hollow (3 subplots) |
| `03e_markers_format_string.py` | Format string shortcuts with markers |
| `03f_markers_every_nth.py` | markevery — show every Nth point |

## 04 — Line Styles

| File | Chart |
|------|-------|
| `04a_line_styles.py` | Solid, dashed, dashdot, dotted (2x2 grid) |
| `04b_line_width.py` | Different line widths |
| `04c_line_colors.py` | Named, hex, and RGB colors |
| `04d_line_multiple_styled.py` | Multiple styled lines (sin, cos, sin*cos) |
| `04e_line_fill_between.py` | Lines with fill_between and alpha |

## 05 — Labels, Titles, and Annotations

| File | Chart |
|------|-------|
| `05a_labels_basic.py` | Basic title, xlabel, ylabel |
| `05b_labels_custom_font.py` | Custom font size, weight, family, color |
| `05c_labels_title_position.py` | Title alignment: left, center, right |
| `05d_labels_legend.py` | Legend with position and style control |
| `05e_labels_annotations.py` | Text annotations with arrows |
| `05f_labels_tick_custom.py` | Custom tick labels (month names) |

## 06 — Grid Lines

| File | Chart |
|------|-------|
| `06a_grid_basic.py` | Basic grid on/off |
| `06b_grid_axis.py` | Grid on specific axis (both, x, y) |
| `06c_grid_custom_style.py` | Grid color, linestyle, linewidth, alpha |
| `06d_grid_line_styles.py` | Different grid line styles (2x2 grid) |
| `06e_grid_major_minor.py` | Major and minor grid lines |
| `06f_grid_colored_bg.py` | Grid with colored background |

## 07 — Subplots

| File | Chart |
|------|-------|
| `07a_subplot_side_by_side.py` | Two subplots side by side (1x2) |
| `07b_subplot_stacked.py` | Stacked subplots (2x1) |
| `07c_subplot_grid.py` | 2x3 grid of trig functions |
| `07d_subplot_mixed_layout.py` | Mixed layout with GridSpec |
| `07e_subplot_shared_axes.py` | Shared Y-axis between subplots |

## 08 — Scatter Plots

| File | Chart |
|------|-------|
| `08a_scatter_basic.py` | Basic scatter (age vs speed) |
| `08b_scatter_two_datasets.py` | Compare two datasets |
| `08c_scatter_colormap.py` | Colormap with varying sizes |
| `08d_scatter_colormaps.py` | Different colormaps comparison (2x2) |
| `08e_scatter_alpha.py` | Transparency with 500 points |
| `08f_scatter_trend_line.py` | Student grades with polyfit trend |

## 09 — Bar Charts

| File | Chart |
|------|-------|
| `09a_bars_basic.py` | Basic vertical bar chart |
| `09b_bars_horizontal.py` | Horizontal bar chart (barh) |
| `09c_bars_custom_colors.py` | Custom colors with value labels |
| `09d_bars_width.py` | Thin vs wide bars (2 subplots) |
| `09e_bars_grouped.py` | Grouped bar chart (3 products) |
| `09f_bars_stacked.py` | Stacked bar chart |
| `09g_bars_error.py` | Bar chart with error bars |

## 10 — Histograms

| File | Chart |
|------|-------|
| `10a_hist_basic.py` | Basic histogram (15 bins) |
| `10b_hist_bins.py` | Different bin counts (5, 15, 50) |
| `10c_hist_density.py` | Density histogram with normal curve |
| `10d_hist_overlapping.py` | Two overlapping histograms |
| `10e_hist_horizontal.py` | Horizontal histogram |
| `10f_hist_cumulative.py` | Cumulative histogram |
| `10g_hist_step.py` | Step histogram (outline + filled) |

## 11 — Pie Charts

| File | Chart |
|------|-------|
| `11a_pie_basic.py` | Basic pie chart |
| `11b_pie_percentages.py` | Pie with percentages (autopct) |
| `11c_pie_customized.py` | Custom colors, explode, shadow |
| `11d_pie_legend.py` | Pie with external legend |
| `11e_pie_donut.py` | Donut chart (center hole) |
| `11f_pie_exploded.py` | All slices slightly exploded |
| `11g_pie_nested.py` | Nested pie (outer + inner ring) |

## 12-14 — Additional Concepts

| File | Chart |
|------|-------|
| `12_boxplot.py` | Box plot (median, quartiles, outliers) |
| `13_estadistico_multi.py` | Histogram + boxplot side by side |
| `14_pandas_seaborn.py` | Pandas + Matplotlib + Seaborn (2x2 dashboard) |

---

## Applied Charts with CSV Data (files 15-53)

Each file creates one chart using CSV datasets from the `09_Pandas/` folder.

### Employees (`employees.csv` + `departments.csv`)

| File | Chart Type |
|------|-----------|
| `15_employees_avg_salary.py` | Horizontal bar — avg salary by dept |
| `16_employees_salary_hist.py` | Histogram — salary distribution |
| `17_employees_dept_pie.py` | Pie — employee distribution by dept |
| `18_employees_salary_box.py` | Box plot — salary by department |

### Players (`players.csv`)

| File | Chart Type |
|------|-----------|
| `19_players_goals_scatter.py` | Scatter — goals vs score by position |
| `20_players_top_scorers.py` | Horizontal bar — top 10 by score |
| `21_players_team_bar.py` | Grouped bar — goals vs attempts by team |
| `22_players_position_pie.py` | Pie — player distribution by position |

### Iris (`iris.csv`)

| File | Chart Type |
|------|-----------|
| `23_iris_sepal_scatter.py` | Scatter — sepal dimensions by species |
| `24_iris_petal_scatter.py` | Scatter — petal dimensions by species |
| `25_iris_feature_hist.py` | Histogram (2x2) — feature distributions |
| `26_iris_feature_box.py` | Box plot (1x4) — features by species |

### Pokémon (`pokemon.csv`)

| File | Chart Type |
|------|-----------|
| `27_pokemon_radar.py` | Radar — compare 4 Pokémon stats |
| `28_pokemon_total_stats.py` | Horizontal bar — total stats sorted |
| `29_pokemon_attack_defense.py` | Grouped bar — attack vs defense |

### Wine Quality (`wine_quality.csv`)

| File | Chart Type |
|------|-----------|
| `30_wine_alcohol_hist.py` | Histogram — alcohol by wine type |
| `31_wine_type_box.py` | Box plot — alcohol and pH by type |
| `32_wine_quality_scatter.py` | Scatter — alcohol vs quality |
| `33_wine_quality_bar.py` | Grouped bar — properties by quality |

### Alcohol Consumption (`alcohol_consumption.csv`)

| File | Chart Type |
|------|-----------|
| `34_alcohol_total_bar.py` | Horizontal bar — total litres by country |
| `35_alcohol_stacked_bar.py` | Stacked bar — beer/spirits/wine |
| `36_alcohol_continent_pie.py` | Pie — avg consumption by continent |
| `37_alcohol_top8_bar.py` | Grouped bar — top 8 countries |

### US Crime Rates (`us_crime_rates.csv`)

| File | Chart Type |
|------|-----------|
| `38_crime_trend_line.py` | Line — violent vs property over time |
| `39_crime_area_chart.py` | Stacked area — crime categories |
| `40_crime_type_panels.py` | Subplots (2x2) — individual crime trends |
| `41_crime_murder_bar.py` | Bar + trend — murder per year |

### Students & Alcohol (`students_alcohol.csv`)

| File | Chart Type |
|------|-----------|
| `42_students_grade_hist.py` | Histogram — final grade distribution |
| `43_students_study_scatter.py` | Scatter — study time vs grade |
| `44_students_school_box.py` | Box plot — grades by school |
| `45_students_alcohol_bar.py` | Bar — grade vs alcohol level |

### Euro 2012 (`euro12.csv`)

| File | Chart Type |
|------|-----------|
| `46_euro12_goals_bar.py` | Horizontal bar — goals by team |
| `47_euro12_shots_bar.py` | Grouped bar — shots on/off target |
| `48_euro12_accuracy_scatter.py` | Scatter — accuracy vs goals |
| `49_euro12_radar.py` | Radar — top 3 teams normalized |

### Auto MPG (`auto_mpg_cars.csv`)

| File | Chart Type |
|------|-----------|
| `50_auto_hp_scatter.py` | Scatter — HP vs MPG by cylinders |
| `51_auto_mpg_hist.py` | Histogram (1x3) — MPG per cylinder |
| `52_auto_mpg_bar.py` | Bar — avg MPG by cylinder count |
| `53_auto_bubble_chart.py` | Bubble — displacement vs MPG |

---

## Requirements

```
matplotlib
numpy
pandas
seaborn    # only for 14_pandas_seaborn.py
scipy      # only for 10c_hist_density.py
```

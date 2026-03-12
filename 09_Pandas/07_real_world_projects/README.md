# Real World Projects - Pandas

This folder contains end-to-end and mini real-world projects for `09_Pandas`.
All scripts are numbered and organized as a progressive portfolio from `01` to `63`.

## Scope

- Folder: `09_Pandas/07_real_world_projects`
- Data sources: `09_Pandas/data`
- Generated artifacts: `09_Pandas/data/exports`

## Project Catalog (01-63)

### Education and Student Performance (01-08)

- `01_lunch_analysis.py` - analyze lunch impact on student performance
- `02_parental_education.py` - parental education effect analysis
- `03_general_analysis.py` - general student score exploration
- `04_ethnic_group.py` - performance analysis by ethnic group
- `05_gender_analysis.py` - performance analysis by gender
- `06_test_preparation.py` - test preparation impact analysis
- `07_students_performance.py` - consolidated student performance KPIs
- `08_main_menu.py` - menu runner for the student-performance scripts

### Exploration and Apply Exercises (09-14)

- `09_chipotle_explore.py` - exploratory analysis on Chipotle-like dataset
- `10_occupation_explore.py` - exploration by occupation
- `11_food_facts.py` - food facts dataset profiling
- `12_alcohol_apply.py` - alcohol consumption apply/grouping practice
- `13_crime_rates_apply.py` - crime rates transformation and aggregation
- `14_baby_names_stats.py` - baby names statistics and trends

### Visualization Projects (15-19)

- `15_chipotle_viz.py` - Chipotle visual analysis
- `16_titanic_viz.py` - Titanic visualization practice
- `17_scores_viz.py` - score distributions and comparative charts
- `18_retail_viz.py` - retail KPI charting
- `19_tips_viz.py` - tips dataset visuals

### Data Cleaning and Deletion Scenarios (20-21)

- `20_iris_delete.py` - cleaning/deletion operations on Iris-style data
- `21_wine_delete.py` - cleaning/deletion operations on wine data

### Practical Business Mini Cases (22-32)

- `22_sales_analysis.py` - base sales analysis
- `23_student_attendance.py` - attendance trends and summary
- `24_personal_budget.py` - personal budget aggregation
- `25_inventory.py` - inventory tracking analysis
- `26_task_tracking.py` - task progress tracking
- `27_construction.py` - construction/project data summary
- `28_system_logs.py` - simple system log analytics
- `29_web_traffic.py` - web traffic summary and trends
- `30_movies_analysis.py` - movie dataset KPIs
- `31_transport_analysis.py` - transport usage analytics
- `32_hr_analysis.py` - HR/people metrics analysis

### Feature Engineering and Data Processing (33-43)

- `33_vectorization.py` - vectorized transformations in Pandas
- `34_chunk_processing.py` - chunked processing for larger files
- `35_export_files.py` - export workflow patterns
- `36_excel_operations.py` - Excel read/write operations with Pandas
- `37_api_data_loading.py` - load API-like data into DataFrames
- `38_api_to_dataframe.py` - API payload normalization to table format
- `39_feature_engineering.py` - derived features creation
- `40_encoding_features.py` - categorical encoding examples
- `41_scaling_features.py` - numerical scaling examples
- `42_customer_segmentation.py` - segmentation-style preprocessing
- `43_sales_forecast_project.py` - baseline forecasting-style project

### Short Practice Scripts (44-49)

- `44_sales_discount.py` - discount calculations with Pandas
- `45_grades_stats.py` - grade summary statistics
- `46_grades_passed.py` - pass/fail analysis
- `47_sales_dataframe.py` - basic sales DataFrame exercises
- `48_balance_months.py` - monthly balance calculations
- `49_stock_quotes.py` - stock quote transformations

### Applied Analytics and Mini Projects (50-57)

- `50_titanic_analysis.py` - Titanic analytical summary
- `51_emissions_analysis.py` - emissions data analysis
- `52_sales_visualization_miniproject.py` - sales charts mini project
- `53_sales_analysis_miniproject.py` - sales analysis mini project
- `54_books_catalog_sqlite.py` - SQLite + Pandas books catalog pipeline
- `55_books_catalog_analysis.py` - books catalog EDA from JSON
- `56_global_banks_regional_analysis.py` - banks KPIs by region and country
- `57_global_banks_regional_visuals.py` - global banks visual reports

### Financial EDA End-to-End Pipeline (58-63)

- `58_financial_data_generator.py` - synthetic finance transactions generator
- `59_financial_cleaning_pipeline.py` - data cleaning and standardization
- `60_financial_descriptive_analysis.py` - category/account/recurrence KPIs
- `61_financial_time_series_analysis.py` - temporal trends and MoM analysis
- `62_financial_anomaly_detection.py` - anomaly detection (P95/P99/IQR/Z-score)
- `63_financial_executive_report.py` - executive text report generation

## Financial Pipeline Execution Order

```bash
python 09_Pandas/07_real_world_projects/58_financial_data_generator.py
python 09_Pandas/07_real_world_projects/59_financial_cleaning_pipeline.py
python 09_Pandas/07_real_world_projects/60_financial_descriptive_analysis.py
python 09_Pandas/07_real_world_projects/61_financial_time_series_analysis.py
python 09_Pandas/07_real_world_projects/62_financial_anomaly_detection.py
python 09_Pandas/07_real_world_projects/63_financial_executive_report.py
```

## Main Financial Outputs

### Data files

- `09_Pandas/data/financial_transactions_raw.csv`
- `09_Pandas/data/financial_transactions_clean.csv`

### Exported tables

- `09_Pandas/data/exports/financial_summary_by_category.csv`
- `09_Pandas/data/exports/financial_pareto_by_category.csv`
- `09_Pandas/data/exports/financial_summary_by_account.csv`
- `09_Pandas/data/exports/financial_summary_recurring_vs_discretionary.csv`
- `09_Pandas/data/exports/financial_monthly_totals.csv`
- `09_Pandas/data/exports/financial_weekday_totals.csv`
- `09_Pandas/data/exports/financial_mom_growth.csv`
- `09_Pandas/data/exports/financial_category_monthly_trend.csv`
- `09_Pandas/data/exports/financial_anomalies.csv`
- `09_Pandas/data/exports/financial_anomalies_flagged.csv`
- `09_Pandas/data/exports/anomalies_flagged.csv`

### Exported charts and report

- `09_Pandas/data/exports/financial_monthly_totals.png`
- `09_Pandas/data/exports/financial_daily_rolling4w.png`
- `09_Pandas/data/exports/financial_outlier_detection.png`
- `09_Pandas/data/exports/executive_summary.txt`

## Notes

- Scripts follow numeric naming for easy learning progression.
- Most scripts are independent; run a script directly with `python <script_name.py>`.
- Financial scripts `58-63` are sequential and should be run in order.
# Financial EDA Project Plan

## Objective
Build an end-to-end **Financial Exploratory Data Analysis (EDA)** project focused on:

- reliable data cleaning,
- meaningful business insights,
- anomaly detection,
- reproducible charts and reports,
- optional SQL integration.

This document defines the project structure and the files we are creating inside
`09_Pandas/07_real_world_projects`.

---

## Scope

We are working specifically in:

- `09_Pandas/07_real_world_projects`
- `09_Pandas/data`
- `09_Pandas/data/exports`

---

## Repository Structure (Project-Centric)

```text
09_Pandas/
├── 07_real_world_projects/
│   ├── README.md                                    # This project guide
│   ├── 54_books_catalog_sqlite.py                   # SQLite + Pandas workflow
│   ├── 55_books_catalog_analysis.py                 # Books EDA from JSON
│   ├── 56_global_banks_regional_analysis.py         # Regional/country KPI analysis
│   ├── 57_global_banks_regional_visuals.py          # Regional visual reporting
│   ├── 58_financial_data_generator.py               # Synthetic finance dataset generator
│   ├── 59_financial_cleaning_pipeline.py            # Data cleaning and normalization
│   ├── 60_financial_descriptive_analysis.py         # Grouped KPI and Pareto analysis
│   ├── 61_financial_time_series_analysis.py         # Temporal analysis and trend exports
│   ├── 62_financial_anomaly_detection.py            # Multi-method outlier detection
│   └── 63_financial_executive_report.py             # Executive summary report builder
│
└── data/
    ├── bancos.csv
    ├── exam_data.json
    ├── students_exam_dataset_1000_*.csv
    └── exports/
        ├── banks_ranking_by_region.csv
        ├── banks_volume_by_country.csv
        ├── banks_leader_by_region.csv
        ├── banks_volume_by_region.png
        ├── banks_top10_countries_volume.png
        ├── banks_top10_avg_close.png
        ├── financial_anomalies.csv
        ├── financial_anomalies_flagged.csv
        ├── anomalies_flagged.csv
        ├── financial_summary_by_category.csv
        ├── financial_pareto_by_category.csv
        ├── financial_summary_by_account.csv
        ├── financial_summary_recurring_vs_discretionary.csv
        ├── financial_monthly_totals.csv
        ├── financial_weekday_totals.csv
        ├── financial_mom_growth.csv
        ├── financial_category_monthly_trend.csv
        ├── financial_monthly_totals.png
        ├── financial_daily_rolling4w.png
        ├── financial_outlier_detection.png
        └── executive_summary.txt
```

---

## Workflow

### 1) Data Generation
- Generate realistic transaction records with controlled noise.
- Include missing values, duplicates, and extreme values for cleaning practice.

### 2) Data Cleaning
- Standardize categories and types.
- Handle nulls and duplicates.
- Normalize amount fields and validate constraints.

### 3) Descriptive Analysis
- Compute totals, averages, counts, and contribution percentages by category.
- Rank top categories and major spending drivers.

### 4) Time-Series Analysis
- Extract month/weekday/period features.
- Analyze trend, seasonality, and spending spikes.

### 5) Anomaly Detection
- Flag suspicious transactions using percentile and z-score logic.
- Export an audit-ready anomaly table.

### 6) Reporting
- Export visuals and summary CSV files.
- Produce a concise executive summary for stakeholders.

---

## Implemented Pipeline Files

The full financial EDA pipeline is now implemented with these files:

1. `58_financial_data_generator.py`
2. `59_financial_cleaning_pipeline.py`
3. `60_financial_descriptive_analysis.py`
4. `61_financial_time_series_analysis.py`
5. `62_financial_anomaly_detection.py`
6. `63_financial_executive_report.py`

Each file should do one clear task and pass data to the next stage.

---

## Execution Order

```bash
python 09_Pandas/07_real_world_projects/58_financial_data_generator.py
python 09_Pandas/07_real_world_projects/59_financial_cleaning_pipeline.py
python 09_Pandas/07_real_world_projects/60_financial_descriptive_analysis.py
python 09_Pandas/07_real_world_projects/61_financial_time_series_analysis.py
python 09_Pandas/07_real_world_projects/62_financial_anomaly_detection.py
python 09_Pandas/07_real_world_projects/63_financial_executive_report.py
```

---

## Deliverables

- Clean dataset ready for analytics
- Category and country/regional KPI tables
- Time-trend and anomaly outputs
- Chart package in `09_Pandas/data/exports`
- Executive summary report for portfolio presentation

---

## Success Criteria

- Reproducible scripts with deterministic outputs when seeded
- Clean separation between generation, cleaning, analysis, and reporting
- Exported artifacts usable in GitHub portfolio and LinkedIn posts
# 📊 Financial EDA Portfolio Project

> A production-quality **Exploratory Data Analysis** pipeline for personal and family finance data —
> combining rigorous data engineering, statistical analysis, anomaly detection, and automated reporting.

---

## 🎯 Project Goal

Build a robust end-to-end EDA project that demonstrates real-world data skills across the full analytics lifecycle:

| Pillar | What it covers |
|---|---|
| **Data Engineering** | Cleaning, transformation, validation, and schema enforcement |
| **Statistical Analysis** | Descriptive stats, distributions, correlations, and trend detection |
| **Anomaly Detection** | Outlier isolation, percentile thresholds, and fraud-ready flagging |
| **Time-Series Analysis** | Temporal feature extraction, seasonality, and spending velocity |
| **Automated Reporting** | KPI summaries, chart exports, and dashboard-ready CSV outputs |
| **Database Integration** | Full ingestion-to-analytics pipeline with SQLAlchemy + PostgreSQL |

---

## 🛠 Technology Stack

### Core
| Library | Role |
|---|---|
| `Python 3.10+` | Runtime |
| `Pandas` | Data manipulation and analysis |
| `NumPy` | Numerical operations and array math |
| `Matplotlib` | Base charting layer |
| `Seaborn` | Statistical visualizations |

### Optional Integrations
| Library | Role |
|---|---|
| `SQLAlchemy` | Unified DB interface (`create_engine`) |
| `PostgreSQL` | Production-grade relational storage |
| `psycopg2-binary` | PostgreSQL driver for Python |

### Dev & Reporting
| Tool | Role |
|---|---|
| `Jupyter Notebook` | Exploratory iteration |
| `pytest` | Unit tests for cleaning functions |
| `requirements.txt` | Reproducible environment |

---

## 📁 Repository Structure

```text
09_Pandas/
├── 07_real_world_projects/
│   ├── README.md                                   # This project guide
│   ├── 54_books_catalog_sqlite.py                  # SQLite + Pandas analysis
│   ├── 55_books_catalog_analysis.py                # Books catalog EDA script
│   ├── 56_global_banks_regional_analysis.py        # Regional/country KPI analysis
│   ├── 57_global_banks_regional_visuals.py         # Regional charts export
│   ├── 58_financial_data_generator.py              # Synthetic finance dataset generator
│   ├── 59_financial_cleaning_pipeline.py           # Data cleaning and normalization
│   ├── 60_financial_descriptive_analysis.py        # Grouped KPI and Pareto analysis
│   ├── 61_financial_time_series_analysis.py        # Temporal analysis and trend exports
│   ├── 62_financial_anomaly_detection.py           # Multi-method outlier detection
│   └── 63_financial_executive_report.py            # Executive summary report builder
│
└── data/
    ├── bancos.csv                                  # Source dataset (global banks)
    ├── exam_data.json                              # Example JSON dataset
    ├── students_exam_dataset_1000_*.csv           # Generated practice datasets
    ├── financial_transactions_raw.csv              # Generated raw finance transactions
    ├── financial_transactions_clean.csv            # Cleaned finance transactions
    └── exports/
        ├── banks_ranking_by_region.csv
        ├── banks_volume_by_country.csv
        ├── banks_leader_by_region.csv
        ├── banks_volume_by_region.png
        ├── banks_top10_countries_volume.png
        ├── banks_top10_avg_close.png
        ├── financial_anomalies.csv
        ├── financial_anomalies_flagged.csv
        ├── anomalies_flagged.csv
        ├── financial_summary_by_category.csv
        ├── financial_pareto_by_category.csv
        ├── financial_summary_by_account.csv
        ├── financial_summary_recurring_vs_discretionary.csv
        ├── financial_monthly_totals.csv
        ├── financial_weekday_totals.csv
        ├── financial_mom_growth.csv
        ├── financial_category_monthly_trend.csv
        ├── financial_monthly_totals.png
        ├── financial_daily_rolling4w.png
        ├── financial_outlier_detection.png
        └── executive_summary.txt
```

---

## 🔄 End-to-End Workflow

### Stage 1 — Data Generation

Synthesize a realistic finance dataset that mirrors real-world data quality issues:

```python
# Injected noise types
noise = {
    "missing_values"         : "~8% of amount and category fields",
    "sign_errors"            : "~3% of expense rows have positive sign",
    "outlier_transactions"   : "~2% of rows exceed 3× category mean",
    "inconsistent_labels"    : "e.g. 'food', 'Food', 'FOOD' → same category",
    "duplicate_rows"         : "~1% exact or near-duplicate entries",
    "date_format_variance"   : "mixed formats: YYYY-MM-DD, MM/DD/YY, etc.",
}
```

**Recommended fields:**

| Column | Type | Notes |
|---|---|---|
| `transaction_id` | `str` | UUID |
| `date` | `datetime` | Mixed format at source |
| `description` | `str` | Free text, vendor name |
| `category` | `str` | Inconsistent casing at source |
| `amount` | `float` | Sign errors present |
| `account` | `str` | Checking / Savings / Credit |
| `is_recurring` | `bool` | Rent, subscriptions, etc. |

---

### Stage 2 — Data Cleaning (Scrubbing)

All cleaning is encapsulated in `src/clean.py` as pure, testable functions.

```python
# Key cleaning operations
df['date']     = pd.to_datetime(df['date'], infer_datetime_format=True)
df['category'] = df['category'].str.strip().str.title()
df['amount']   = df['amount'].abs()                        # correct sign errors
df             = df.drop_duplicates(subset=['transaction_id'])
df['amount']   = df['amount'].fillna(df['amount'].median())
df['category'] = df['category'].fillna('Uncategorized')
```

**Cleaning checklist:**

- [x] Parse and standardize all date formats
- [x] Normalize category labels (strip, title-case)
- [x] Correct sign errors with `abs()` on expense amounts
- [x] Fill or flag missing values by column type
- [x] Remove duplicate rows by `transaction_id`
- [x] Validate `amount > 0` after correction
- [x] Optional: regex validation on `transaction_id` format

**Expected output:** `09_Pandas/data/financial_transactions_clean.csv` — a fully trusted dataset.

---

### Stage 3 — Descriptive Analysis

Answer core business questions with grouped aggregations:

```python
# Spending by category
summary = df.groupby('category')['amount'].agg(
    total='sum', mean='mean', count='count', pct_of_total=lambda x: x.sum() / df['amount'].sum()
).sort_values('total', ascending=False)
```

**Key questions answered:**

| Question | Method |
|---|---|
| Which categories consume most of the budget? | `groupby + sum + rank` |
| What is the average transaction value? | `describe()` |
| How concentrated is total spending? | Cumulative % / Pareto |
| Which account drives most outflows? | `groupby('account').sum()` |
| What share is recurring vs discretionary? | `groupby('is_recurring').sum()` |

---

### Stage 4 — Time-Series Analysis

Extract temporal features and analyze spending velocity over time:

```python
df['month']    = df['date'].dt.to_period('M')
df['weekday']  = df['date'].dt.day_name()
df['week']     = df['date'].dt.isocalendar().week
df['quarter']  = df['date'].dt.quarter

monthly = df.groupby('month')['amount'].sum()
weekly  = df.groupby('week')['amount'].sum()
```

**Patterns to detect:**

- Monthly seasonality (higher spending in Dec, Jan)
- Weekday spending profile (weekend vs weekday)
- Rolling 4-week average vs raw spending
- Month-over-month growth rate
- Category trends over time (is dining spend increasing?)

**Recommended visuals:**

| Chart | Insight |
|---|---|
| Line chart — daily/weekly trend | Spending velocity and spikes |
| Bar chart — monthly totals | Seasonality and budget tracking |
| Heatmap — weekday × category | Behavioral patterns |
| Area chart — category over time | Share-of-wallet shift |

---

### Stage 5 — Anomaly Detection

Flag suspicious or extreme transactions for audit:

```python
# Percentile thresholds
p95 = df['amount'].quantile(0.95)
p99 = df['amount'].quantile(0.99)

df['anomaly_flag'] = df['amount'] > p95

# Z-score method (per category)
df['z_score'] = df.groupby('category')['amount'].transform(
    lambda x: (x - x.mean()) / x.std()
)
df['outlier'] = df['z_score'].abs() > 3
```

**Detection methods:**

| Method | Use case |
|---|---|
| `P95 / P99` percentile threshold | Simple global threshold |
| IQR (interquartile range) | Robust to skewed distributions |
| Z-score per category | Category-aware anomaly detection |
| Boxplot visual inspection | Quick exploratory check |

**Output:** `data/exports/anomalies_flagged.csv` — a ready-made audit table.

---

## 📋 Automated Reporting Layer

`63_financial_executive_report.py` generates the executive reporting package after the analysis stages.

```text
executive_summary.txt
─────────────────────────────────────────
Report Date       : 2026-03-11
Period Covered    : 2025-01-01 → 2025-12-31
Total Transactions: 1,248
Total Spending    : $42,310.75
Avg Transaction   : $33.90
Top Category      : Housing (28.4%)
Anomalies Flagged : 24 transactions (P95 threshold: $312.50)
MoM Growth (Dec)  : +8.2%
─────────────────────────────────────────
```

**All exports written to `data/exports/`:**

| File | Content |
|---|---|
| `financial_summary_by_category.csv` | Grouped category totals, averages, counts, share of total |
| `financial_pareto_by_category.csv` | Cumulative spending concentration (Pareto view) |
| `financial_summary_by_account.csv` | Spending profile by account |
| `financial_summary_recurring_vs_discretionary.csv` | Recurring vs discretionary spending split |
| `financial_monthly_totals.csv` | Monthly totals with MoM growth |
| `financial_weekday_totals.csv` | Spending profile by weekday |
| `financial_category_monthly_trend.csv` | Category trends over time |
| `financial_anomalies_flagged.csv` / `anomalies_flagged.csv` | Audit-ready anomaly table |
| `financial_monthly_totals.png` | Monthly trend visualization |
| `financial_daily_rolling4w.png` | Daily totals vs 4-week rolling average |
| `financial_outlier_detection.png` | Category-level outlier boxplot |
| `executive_summary.txt` | KPI snapshot — plain text |

---

## 🗄 PostgreSQL Integration Pipeline

`src/db_pipeline.py` demonstrates a complete data lifecycle:

```python
from sqlalchemy import create_engine

# Swap engine string to target any supported DB
engine = create_engine('postgresql://user:pass@localhost:5432/finance_db')
# engine = create_engine('sqlite:///finance.db')          # local dev
# engine = create_engine('mysql+mysqldb://user:pass@host/finance_db')

# Ingest raw data
df_raw.to_sql('transactions_raw', engine, if_exists='replace', index=False)

# Persist clean analytics table
df_clean.to_sql('transactions_clean', engine, if_exists='replace', index=False)

# Persist anomaly audit table
df_anomalies.to_sql('anomalies', engine, if_exists='replace', index=False)
```

**Pipeline stages:**

```
[CSV / Mock Generator]
        ↓
  [PostgreSQL raw table]
        ↓
  [Pandas: clean + enrich]
        ↓
  [PostgreSQL clean table]
        ↓
  [Pandas: EDA + aggregations]
        ↓
  [Exports: charts + CSVs + summary]
```

---

## ✅ Testing

Core cleaning functions are unit-tested in `tests/test_clean.py`:

```python
def test_sign_correction():
    df = pd.DataFrame({'amount': [-50.0, 30.0, -10.0]})
    result = correct_signs(df)
    assert (result['amount'] >= 0).all()

def test_category_normalization():
    df = pd.DataFrame({'category': ['food', 'FOOD', ' Food ']})
    result = normalize_categories(df)
    assert result['category'].nunique() == 1
```

---

## 🚀 How to Run

```bash
# 1. Clone and set up environment
git clone https://github.com/youruser/financial-eda.git
cd financial-eda
pip install -r requirements.txt

# 2. Run the implemented financial EDA pipeline
python 09_Pandas/07_real_world_projects/58_financial_data_generator.py
python 09_Pandas/07_real_world_projects/59_financial_cleaning_pipeline.py
python 09_Pandas/07_real_world_projects/60_financial_descriptive_analysis.py
python 09_Pandas/07_real_world_projects/61_financial_time_series_analysis.py
python 09_Pandas/07_real_world_projects/62_financial_anomaly_detection.py
python 09_Pandas/07_real_world_projects/63_financial_executive_report.py

# 5. Optional — run PostgreSQL pipeline
python src/db_pipeline.py

# 6. Run tests
pytest tests/
```

---

## 📦 requirements.txt

```text
pandas>=2.0
numpy>=1.25
matplotlib>=3.7
seaborn>=0.12
sqlalchemy>=2.0
psycopg2-binary>=2.9
pytest>=7.4
jupyter>=1.0
```

---

## 💼 Portfolio Value

| Skill demonstrated | How |
|---|---|
| Data engineering | Multi-stage cleaning pipeline with testable functions |
| Statistical thinking | Distributions, percentiles, z-scores, correlations |
| Business communication | Executive summary with plain-language KPIs |
| Software engineering | Modular `src/` structure, unit tests, reproducible env |
| Database fluency | Full SQLAlchemy pipeline across multiple DB targets |
| Data storytelling | 5 chart types, each mapped to a specific business question |

This project is designed for **GitHub** and **LinkedIn** presentation — it combines technical depth, clean code structure, and clear business relevance in a format that is immediately legible to both technical reviewers and non-technical stakeholders.
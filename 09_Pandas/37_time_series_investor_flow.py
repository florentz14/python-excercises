# -------------------------------------------------
# File Name: 37_time_series_investor_flow.py
# Author: Florentino Báez
# Date: Pandas
# Description: Analyze US Investor Fund Flow Time Series. Practice period-based
#              indexing, cumulative sums, percentage calculations, and trend
#              analysis on quarterly investment data.
# -------------------------------------------------

import pandas as pd
import numpy as np

# -------------------------------------------------
# Create DataFrame with quarterly dates for 5 years
# -------------------------------------------------
np.random.seed(99)
quarters = pd.date_range(start="2019-01-01", end="2023-12-31", freq="QS")
n = len(quarters)

# Generate realistic fund flow data (millions): some positive, some negative
domestic = np.random.normal(12000, 8000, n).round(0)
foreign = np.random.normal(3000, 2000, n).round(0)
bonds = np.random.normal(5000, 4000, n).round(0)
money_market = np.random.normal(-2000, 3000, n).round(0)
total_flow = domestic + foreign + bonds + money_market

df = pd.DataFrame({
    "Domestic_Equity": domestic,
    "Foreign_Equity": foreign,
    "Bonds": bonds,
    "Money_Market": money_market,
    "Total_Flow": total_flow
}, index=quarters)
df.index.name = "Quarter"
print("Investor flow data (millions, first 5 quarters):")
print(df.head())
print()

# -------------------------------------------------
# Calculate cumulative flow using cumsum()
# -------------------------------------------------
df["Cumulative_Flow"] = df["Total_Flow"].cumsum()
print("Cumulative total flow:")
print(df[["Total_Flow", "Cumulative_Flow"]].head(8))
print()

# -------------------------------------------------
# Calculate percentage of total for each category (per row)
# -------------------------------------------------
flow_cols = ["Domestic_Equity", "Foreign_Equity", "Bonds", "Money_Market"]
row_total = df[flow_cols].sum(axis=1)
for col in flow_cols:
    df[f"Pct_{col}"] = (df[col] / row_total * 100).round(2)
print("Percentage of total per category (sample):")
print(df[["Domestic_Equity", "Pct_Domestic_Equity", "Foreign_Equity", "Pct_Foreign_Equity"]].head(3))
print()

# -------------------------------------------------
# Resample or group by year, calculate annual totals
# -------------------------------------------------
df["Year"] = df.index.year
annual = df.groupby("Year")[["Domestic_Equity", "Foreign_Equity", "Bonds", "Money_Market", "Total_Flow"]].sum()
print("Annual totals by category:")
print(annual)
print()

# -------------------------------------------------
# Calculate quarter-over-quarter change
# -------------------------------------------------
df["Total_Flow_QoQ"] = df["Total_Flow"].pct_change()
print("Quarter-over-quarter change in Total_Flow:")
print(df[["Total_Flow", "Total_Flow_QoQ"]].head(6))
print()

# -------------------------------------------------
# Find quarters with net outflows (Total_Flow < 0)
# -------------------------------------------------
outflows = df[df["Total_Flow"] < 0]
print("Quarters with net outflows:")
print(outflows[["Total_Flow"]])
print()

# -------------------------------------------------
# Calculate rolling 4-quarter average
# -------------------------------------------------
df["Rolling_4Q_Avg"] = df["Total_Flow"].rolling(window=4).mean()
print("Rolling 4-quarter average (last 5):")
print(df[["Total_Flow", "Rolling_4Q_Avg"]].tail(5))
print()

# -------------------------------------------------
# Identify trend: is money moving from equity to bonds?
# -------------------------------------------------
df["Equity_Total"] = df["Domestic_Equity"] + df["Foreign_Equity"]
annual_equity = df.groupby("Year")["Equity_Total"].sum()
annual_bonds = df.groupby("Year")["Bonds"].sum()
equity_share = annual_equity / (annual_equity + annual_bonds)
bonds_share = annual_bonds / (annual_equity + annual_bonds)
print("Annual equity vs bonds (totals):")
print(pd.DataFrame({"Equity": annual_equity, "Bonds": annual_bonds}))
print("Equity share by year:", equity_share.values)
print("Bonds share by year:", bonds_share.values)
if equity_share.iloc[-1] < equity_share.iloc[0] and bonds_share.iloc[-1] > bonds_share.iloc[0]:
    print("Trend: Money appears to be moving from equity to bonds over the period.")
else:
    print("Trend: No clear shift from equity to bonds in this sample.")
print()

# -------------------------------------------------
# describe() and corr() for summary statistics
# -------------------------------------------------
print("Describe:")
print(df[flow_cols + ["Total_Flow"]].describe())
print("Correlation between flow categories:")
print(df[flow_cols].corr())
print()

# -------------------------------------------------
# Show the year with the most investment inflow
# -------------------------------------------------
year_inflow = annual["Total_Flow"].idxmax()
print("Year with the most investment inflow:", year_inflow, "Total:", annual.loc[year_inflow, "Total_Flow"])

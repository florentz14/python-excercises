# -------------------------------------------------
# File Name: 97_emissions_analysis.py
# Author: Florentino Báez
# Date: Pandas
# Description: Madrid emissions: reshape, dates, summaries.
# -------------------------------------------------

from datetime import datetime
from pathlib import Path

import pandas as pd

DATA = Path(__file__).parent.parent / "data"

# 1. Load the 4 files
dfs = []
for year in [2016, 2017, 2018, 2019]:
    df = pd.read_csv(DATA / f"emisiones-{year}.csv")
    dfs.append(df)
df = pd.DataFrame(pd.concat(dfs, ignore_index=True))

# 2. Filter columns: ESTACION, MAGNITUD, AÑO, MES, D01, D02, ...
fixed_cols = ["ESTACION", "MAGNITUD", "AÑO", "MES"]
day_cols = [c for c in df.columns if c.startswith("D")]
df = df[fixed_cols + day_cols]

# 3. Reshape: days in a single column
df_melt = df.melt(
    id_vars=fixed_cols,
    value_vars=day_cols,
    var_name="DAY",
    value_name="EMISSION",
)
df_melt["DAY"] = df_melt["DAY"].str.replace("D", "").astype(int)

# 4. Date column
df_melt["date"] = df_melt.apply(
    lambda r: datetime(r["AÑO"], r["MES"], r["DAY"]),
    axis=1,
)
# Validate date (days 1-28 to avoid short months)
df_melt = pd.DataFrame(df_melt[df_melt["DAY"] <= 28])
df_melt["date"] = pd.to_datetime(df_melt["date"], errors="coerce")

# 5. Drop invalid dates and sort
df_melt = pd.DataFrame(df_melt[df_melt["date"].notna()])
df_melt_rows = sorted(
    df_melt.itertuples(index=False),
    key=lambda row: (int(row[0]), int(row[1]), pd.Timestamp(row[6])),
)
df_melt = pd.DataFrame(
    df_melt_rows, columns=["ESTACION", "MAGNITUD", "AÑO", "MES", "DAY", "EMISSION", "date"]
)

print("=" * 60)
print("EXERCISE 8: MADRID EMISSIONS")
print("=" * 60)

# 6. Stations and pollutants
print("\n6. Stations:", df_melt["ESTACION"].unique().tolist())
print("   Pollutants (MAGNITUD):", df_melt["MAGNITUD"].unique().tolist())


def emissions_range(station, pollutant, start_date, end_date):
    """Returns Series of emissions for station, pollutant and date range."""
    mask = (
        (df_melt["ESTACION"] == station)
        & (df_melt["MAGNITUD"] == pollutant)
        & (df_melt["date"] >= start_date)
        & (df_melt["date"] <= end_date)
    )
    return df_melt.loc[mask].set_index("date")["EMISSION"]


# 7. Example
s = emissions_range(28079004, 8, pd.Timestamp("2016-01-01"), pd.Timestamp("2016-02-28"))
print("\n7. Emissions station 28079004, pollutant 8 (2016-01 to 2016-02):")
print(s.head(8))

# 8. Summary by pollutant
print("\n8. Descriptive summary by pollutant:")
print(df_melt.groupby("MAGNITUD")["EMISSION"].describe())

# 9. Summary by station (district)
print("\n9. Summary by station:")
print(df_melt.groupby("ESTACION")["EMISSION"].agg(["min", "max", "mean"]))


def station_pollutant_summary(station, pollutant):
    """Descriptive summary of emissions for given station and pollutant."""
    mask = (df_melt["ESTACION"] == station) & (df_melt["MAGNITUD"] == pollutant)
    return df_melt.loc[mask, "EMISSION"].describe()


# 10.
print("\n10. Summary station 28079004, pollutant 8:")
print(station_pollutant_summary(28079004, 8))


def monthly_means(pollutant, year):
    """Monthly means of pollutant and year for all stations."""
    mask = (df_melt["MAGNITUD"] == pollutant) & (df_melt["AÑO"] == year)
    return df_melt.loc[mask].groupby(["ESTACION", "MES"])["EMISSION"].mean().unstack(level=0)


# 11.
print("\n11. Monthly means pollutant 8, 2016:")
print(monthly_means(8, 2016))


def station_monthly_means(station):
    """DataFrame with monthly means per pollutant for a station."""
    mask = df_melt["ESTACION"] == station
    return df_melt.loc[mask].groupby(["MAGNITUD", "MES"])["EMISSION"].mean().unstack(level=0)


# 12.
print("\n12. Monthly means by pollutant, station 28079004:")
print(station_monthly_means(28079004))

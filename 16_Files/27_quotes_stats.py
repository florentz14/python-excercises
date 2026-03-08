# -------------------------------------------------
# File Name: 27_quotes_stats.py
# Description: Load quotes.csv to dict; create CSV with min, max, mean per column
# -------------------------------------------------

import csv
from pathlib import Path

DATA = Path(__file__).parent / "data" / "quotes.csv"


def load_quotes(filepath: str | Path) -> dict:
    """Load quotes CSV and return dict with data by columns."""
    result = {}
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            for k, v in row.items():
                if k not in result:
                    result[k] = []
                if k == "Name":
                    result[k].append(v)
                else:
                    try:
                        val = v.replace(",", ".").replace(" ", "")
                        result[k].append(float(val))
                    except ValueError:
                        result[k].append(v)
    return result


def create_stats_csv(data: dict, output_path: str | Path) -> None:
    """Create CSV with min, max, mean for each numeric column."""
    rows = []
    for col, values in data.items():
        numeric = [x for x in values if isinstance(x, (int, float))]
        if numeric:
            rows.append({
                "Column": col,
                "Min": min(numeric),
                "Max": max(numeric),
                "Mean": sum(numeric) / len(numeric),
            })

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Column", "Min", "Max", "Mean"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    d = load_quotes(DATA)
    print("Loaded columns:", list(d.keys()))
    create_stats_csv(d, Path(__file__).parent / "data" / "quotes_summary.csv")

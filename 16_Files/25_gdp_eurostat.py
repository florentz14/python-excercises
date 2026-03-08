# -------------------------------------------------
# File Name: 25_gdp_eurostat.py
# Description: Fetch EU GDP per capita from Eurostat, show by country initials
# -------------------------------------------------

import urllib.request


GDP_URL = (
    "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing"
    "?file=data/sdg_08_10.tsv.gz&unzip=true"
)


def fetch_gdp_data() -> str:
    """Fetch GDP TSV from Eurostat."""
    with urllib.request.urlopen(GDP_URL, timeout=30) as resp:
        return resp.read().decode("utf-8")


def parse_gdp_tsv(text: str) -> dict:
    """Parse Eurostat TSV. Returns dict: country_code -> {year: value}."""
    lines = text.strip().split("\n")
    if not lines:
        return {}

    header = lines[0]
    if "\\" in header:
        dim_part, time_part = header.split("\\", 1)
        years = [y.strip() for y in time_part.split("\t") if y.strip()]
    else:
        parts = header.split("\t")
        years = parts[1:] if len(parts) > 1 else []

    result = {}
    for line in lines[1:]:
        parts = line.split("\t")
        if not parts:
            continue
        country_code = parts[0].split(",")[-1].strip() if "," in parts[0] else parts[0].strip()
        values = []
        for v in parts[1 : 1 + len(years)]:
            v = v.strip().replace(":", "").replace(" ", "")
            try:
                values.append(float(v) if v else None)
            except ValueError:
                values.append(None)

        result[country_code] = dict(zip(years, values)) if years else {}

    return result


def main() -> None:
    initials = input("Enter country initials (e.g. ES, DE, FR): ").strip().upper()
    if not initials:
        initials = "ES"

    try:
        text = fetch_gdp_data()
    except Exception as e:
        print(f"Error fetching data: {e}")
        return

    data = parse_gdp_tsv(text)
    if initials not in data:
        print(f"Country '{initials}' not found. Available: {sorted(data.keys())[:20]}...")
        return

    print(f"\nGDP per capita - {initials}")
    print("-" * 30)
    for year, val in sorted(data[initials].items()):
        if val is not None:
            print(f"  {year}: {val:,.0f}")


if __name__ == "__main__":
    main()

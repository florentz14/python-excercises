# -------------------------------------------------
# File Name: 60_outliers_zscore.py
# Description: Return outliers (z-score > 3 or < -3)
# -------------------------------------------------

import statistics


def outliers_zscore(sample: list[float]) -> list[float]:
    """Return values with z-score > 3 or < -3."""
    if len(sample) < 2:
        return []
    mu = statistics.mean(sample)
    sigma = statistics.stdev(sample)
    if sigma == 0:
        return []
    return [
        x for x in sample
        if (x - mu) / sigma > 3 or (x - mu) / sigma < -3
    ]


if __name__ == "__main__":
    data = [1, 2, 2, 3, 3, 3, 4, 4, 100]  # 100 may be outlier depending on spread
    print("Sample 1:", outliers_zscore(data))
    data2 = [10, 10, 10, 10, 10, 100]  # 100 is clear outlier
    print("Sample 2:", outliers_zscore(data2))

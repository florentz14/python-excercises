# -------------------------------------------------
# File Name: 13_stock_span_problem.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Stock span problem. Days until price greater than current.
# -------------------------------------------------

def stock_span(prices: list[int]) -> list[int]:
    """
    Returns span for each day using monotonic decreasing stack.
    Span[i] = number of consecutive days (including i) where price <= prices[i].
    """
    n = len(prices)
    spans = [1] * n
    stack = []  # monotonic decreasing: (index, price)

    for i in range(n):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        spans[i] = i - stack[-1] if stack else i + 1
        stack.append(i)

    return spans


if __name__ == "__main__":
    print("=== Stock Span Problem ===\n")

    prices = [100, 80, 60, 70, 60, 75, 85]
    spans = stock_span(prices)

    print(f"Prices: {prices}")
    print(f"Spans:  {spans}")
    print("\nExplanation:")
    for i, (p, s) in enumerate(zip(prices, spans)):
        print(f"  Day {i}: price={p} -> span={s} (consecutive days with price <= {p})")

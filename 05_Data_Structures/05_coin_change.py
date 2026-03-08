# -------------------------------------------------
# File Name: 05_coin_change.py
# Author: Florentino Báez
# Date: 05_Data_Structures
# Description: Coin Change problem using greedy or dynamic programming. Finds minimum coins to make a given amount.
# -------------------------------------------------

def coin_change_greedy(coins, amount):
    """
    Makes change with a greedy strategy: use largest coin first.
    Returns: (change_list, remainder) where change_list is [(coin, count), ...]
    """
    coins = sorted(coins, reverse=True)
    change = []
    remaining = amount

    for coin in coins:
        if remaining >= coin:
            count = remaining // coin
            change.append((coin, count))
            remaining -= count * coin
        if remaining == 0:
            break

    return change, remaining


if __name__ == "__main__":
    print("=== Greedy Algorithms: Coin Change ===\n")

    canonical_coins = [1, 5, 10, 25, 50, 100]
    amount = 287

    print(f"Available coins: {canonical_coins}")
    print(f"Amount to change: {amount}")

    change, remainder = coin_change_greedy(canonical_coins, amount)
    print("\nChange (coin, count):")
    total = 0
    for coin, count in change:
        print(f"  {coin}: {count} coin(s)")
        total += coin * count
    print(f"Total: {total}")
    if remainder > 0:
        print(f"Unchanged remainder: {remainder}")

    print("\n[WARNING] Example where Greedy is NOT optimal:")
    non_canonical = [1, 3, 4]
    amount_fail = 6
    change_greedy, _ = coin_change_greedy(non_canonical, amount_fail)
    print(f"Coins: {non_canonical}, Amount: {amount_fail}")
    print(f"Greedy uses: {sum(c for _, c in change_greedy)} coins")
    print("Optimal would be: 2 coins (3+3)")

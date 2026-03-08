# -------------------------------------------------
# File Name: 10_prefix_evaluation.py
# Author: Florentino Báez
# Date: 12_Stacks
# Description: Prefix expression evaluation. Stack or recursive evaluation.
# -------------------------------------------------

def eval_prefix(tokens: list[str]) -> float:
    """
    Evaluate prefix expression. Scan from right to left.
    Example: ["*", "+", "2", "3", "5"] -> 25
    """
    stack = []
    for t in reversed(tokens):
        if t in "+-*/":
            a, b = stack.pop(), stack.pop()
            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            elif t == "/":
                stack.append(a / b)
        else:
            stack.append(float(t))
    return stack[0]


def eval_prefix_string(expr: str) -> float:
    """Evaluate prefix from space-separated string."""
    return eval_prefix(expr.split())


if __name__ == "__main__":
    print("=" * 55)
    print("Prefix Evaluation")
    print("=" * 55)

    # * + 2 3 5 = (2+3)*5 = 25
    tokens = ["*", "+", "2", "3", "5"]
    result = eval_prefix(tokens)
    print(f"  {tokens} -> {result}")

    # - * 4 5 6 = 4*5-6 = 14
    tokens2 = ["-", "*", "4", "5", "6"]
    print(f"  {tokens2} -> {eval_prefix(tokens2)}")

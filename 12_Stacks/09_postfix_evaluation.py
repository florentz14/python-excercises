"""
12_Stacks - Postfix (RPN) Expression Evaluation
=================================================
Evaluate Reverse Polish Notation: operands → push, operator → pop 2, compute, push.
Used in: compilers, calculators, interpreters.
"""


def eval_postfix(tokens: list[str]) -> float:
    """
    Evaluate postfix expression. Tokens: numbers and +, -, *, /
    Example: ["2", "3", "+", "5", "*"] -> 25
    """
    stack = []
    for t in tokens:
        if t in "+-*/":
            b, a = stack.pop(), stack.pop()
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


def eval_postfix_string(expr: str) -> float:
    """Evaluate postfix from space-separated string."""
    return eval_postfix(expr.split())


if __name__ == "__main__":
    print("=" * 55)
    print("Postfix (RPN) Evaluation")
    print("=" * 55)

    # 2 3 + 5 * = (2+3)*5 = 25
    tokens = ["2", "3", "+", "5", "*"]
    result = eval_postfix(tokens)
    print(f"  {tokens} -> {result}")

    # 4 2 / 3 + = 4/2+3 = 5
    tokens2 = ["4", "2", "/", "3", "+"]
    print(f"  {tokens2} -> {eval_postfix(tokens2)}")

    # From string
    expr = "10 2 8 * + 3 -"
    print(f"  '{expr}' -> {eval_postfix_string(expr)}")

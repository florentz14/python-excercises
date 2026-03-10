# -------------------------------------------------
# File Name: 29_expression_tree_from_postfix.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Build and evaluate expression tree from postfix.
# -------------------------------------------------

"""
============================================================
  EXPRESSION TREE FROM POSTFIX - Python 3.14
  Build a binary expression tree from postfix tokens using stack.

  Example:
    postfix: 3 4 + 2 * 7 /
    infix  : ((3 + 4) * 2) / 7

  Steps:
    - Operand -> push as node
    - Operator -> pop right, pop left, create operator node
    - Push new subtree root back to stack
============================================================
"""

SEPARATOR = "=" * 60
OPERATORS = {"+", "-", "*", "/"}


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


class ExprNode:
    """Node for an expression tree."""

    def __init__(self, value: str) -> None:
        self.value = value
        self.left: "ExprNode | None" = None
        self.right: "ExprNode | None" = None


def build_expression_tree(postfix_tokens: list[str]) -> ExprNode:
    """Build expression tree from postfix token list."""
    stack: list[ExprNode] = []

    for token in postfix_tokens:
        if token not in OPERATORS:
            stack.append(ExprNode(token))
        else:
            right = stack.pop()
            left = stack.pop()
            root = ExprNode(token)
            root.left = left
            root.right = right
            stack.append(root)

    if len(stack) != 1:
        raise ValueError("Invalid postfix expression.")
    return stack[0]


def to_infix(node: ExprNode) -> str:
    if node.left is None and node.right is None:
        return node.value
    return f"({to_infix(node.left)} {node.value} {to_infix(node.right)})"


def to_prefix(node: ExprNode) -> str:
    if node.left is None and node.right is None:
        return node.value
    return f"{node.value} {to_prefix(node.left)} {to_prefix(node.right)}"


def evaluate(node: ExprNode) -> float:
    if node.left is None and node.right is None:
        return float(node.value)
    a = evaluate(node.left)
    b = evaluate(node.right)
    if node.value == "+":
        return a + b
    if node.value == "-":
        return a - b
    if node.value == "*":
        return a * b
    if node.value == "/":
        return a / b
    raise ValueError(f"Unknown operator: {node.value}")


def demo() -> None:
    title("EXPRESSION TREE FROM POSTFIX")

    expressions = [
        ["3", "4", "+", "2", "*", "7", "/"],
        ["5", "1", "2", "+", "4", "*", "+", "3", "-"],
    ]

    for tokens in expressions:
        root = build_expression_tree(tokens)
        print(f"\n  Postfix: {' '.join(tokens)}")
        print(f"  Infix  : {to_infix(root)}")
        print(f"  Prefix : {to_prefix(root)}")
        print(f"  Value  : {evaluate(root)}")


if __name__ == "__main__":
    demo()

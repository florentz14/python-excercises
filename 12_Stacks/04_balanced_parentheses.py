# Balanced Parentheses Checker using Stack

class Stack:
    """Basic stack implementation"""
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop() if not self.is_empty() else None
    
    def peek(self):
        return self.items[-1] if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)


def check_balanced_parentheses(expression):
    """Checks if parentheses, brackets, and braces are balanced"""
    stack = Stack()
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in expression:
        if char in pairs.keys():
            stack.push(char)
        elif char in pairs.values():
            if stack.is_empty():
                return False
            if pairs[stack.pop()] != char:
                return False
    
    return stack.is_empty()


# USAGE EXAMPLES
if __name__ == "__main__":
    print("=" * 50)
    print("BALANCED PARENTHESES CHECKER")
    print("=" * 50)
    test_cases = ["(())", "({[]})", "(()", "{[}]", "", "((a+b)*(c-d))"]
    for expr in test_cases:
        result = check_balanced_parentheses(expr)
        print(f"'{expr}' is balanced: {result}")

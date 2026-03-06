# Infix to Postfix Converter using Stack

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


def infix_to_postfix(expression):
    """Converts infix notation to postfix (Reverse Polish Notation)"""
    stack = Stack()
    output = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    for char in expression.replace(" ", ""):
        if char.isalnum():  # Operand
            output.append(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '('
        else:  # Operator
            while (not stack.is_empty() and 
                   stack.peek() != '(' and 
                   precedence.get(stack.peek(), 0) >= precedence.get(char, 0)):
                output.append(stack.pop())
            stack.push(char)
    
    while not stack.is_empty():
        output.append(stack.pop())
    
    return ''.join(output)


# USAGE EXAMPLES
if __name__ == "__main__":
    print("=" * 50)
    print("INFIX TO POSTFIX CONVERTER")
    print("=" * 50)
    
    expressions = [
        "A+B*C",
        "(A+B)*C",
        "A+B+C",
        "A*(B+C)/D",
        "A+B*C-D/E",
        "((A+B)*C-(D-E))*(F+G)"
    ]
    
    for expr in expressions:
        print(f"Infix:   {expr}")
        print(f"Postfix: {infix_to_postfix(expr)}")
        print()

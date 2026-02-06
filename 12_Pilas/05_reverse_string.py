# Reverse String Using Stack

class Stack:
    """Basic stack implementation"""
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop() if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0


def reverse_string(text):
    """Reverses a string using a stack"""
    stack = Stack()
    
    # Push all characters onto stack
    for char in text:
        stack.push(char)
    
    # Pop all characters to create reversed string
    reversed_text = ""
    while not stack.is_empty():
        reversed_text += stack.pop()
    
    return reversed_text


# USAGE EXAMPLES
if __name__ == "__main__":
    print("=" * 50)
    print("REVERSE STRING USING STACK")
    print("=" * 50)
    
    test_strings = ["Hello World", "Python", "12345", "racecar"]
    for text in test_strings:
        print(f"Original: '{text}'")
        print(f"Reversed: '{reverse_string(text)}'")
        print()

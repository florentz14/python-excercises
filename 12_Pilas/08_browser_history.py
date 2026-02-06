# Browser History Navigator using Stacks

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


class BrowserHistory:
    """Browser history with back/forward navigation using stacks"""
    def __init__(self, homepage):
        self.current = homepage
        self.back_stack = Stack()
        self.forward_stack = Stack()
    
    def visit(self, url):
        """Visits a new URL"""
        self.back_stack.push(self.current)
        self.current = url
        self.forward_stack = Stack()  # Clear forward history
        print(f"Visiting: {self.current}")
    
    def back(self):
        """Goes back to previous page"""
        if not self.back_stack.is_empty():
            self.forward_stack.push(self.current)
            self.current = self.back_stack.pop()
            print(f"Back to: {self.current}")
            return True
        else:
            print("No previous page")
            return False
    
    def forward(self):
        """Goes forward to next page"""
        if not self.forward_stack.is_empty():
            self.back_stack.push(self.current)
            self.current = self.forward_stack.pop()
            print(f"Forward to: {self.current}")
            return True
        else:
            print("No next page")
            return False
    
    def current_page(self):
        """Returns current page"""
        return self.current


# USAGE EXAMPLES
if __name__ == "__main__":
    print("=" * 50)
    print("BROWSER HISTORY NAVIGATOR")
    print("=" * 50)
    
    browser = BrowserHistory("google.com")
    print(f"Homepage: {browser.current_page()}")
    
    print("\n--- Visiting pages ---")
    browser.visit("youtube.com")
    browser.visit("github.com")
    browser.visit("stackoverflow.com")
    
    print("\n--- Going back ---")
    browser.back()
    browser.back()
    
    print("\n--- Going forward ---")
    browser.forward()
    
    print("\n--- Visiting new page (clears forward history) ---")
    browser.visit("reddit.com")
    
    print("\n--- Trying to go forward (should fail) ---")
    browser.forward()
    
    print("\n--- Going back ---")
    browser.back()
    
    print(f"\nCurrent page: {browser.current_page()}")

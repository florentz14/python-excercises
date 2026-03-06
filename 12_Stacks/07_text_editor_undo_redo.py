# Text Editor with Undo/Redo using Stacks

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


class TextEditor:
    """Simple text editor with undo/redo using stacks"""
    def __init__(self):
        self.text = ""
        self.undo_stack = Stack()
        self.redo_stack = Stack()
    
    def write(self, new_text):
        """Adds text and saves state for undo"""
        self.undo_stack.push(self.text)
        self.text += new_text
        # Clear redo stack when new action is performed
        self.redo_stack = Stack()
    
    def undo(self):
        """Undoes the last write operation"""
        if not self.undo_stack.is_empty():
            self.redo_stack.push(self.text)
            self.text = self.undo_stack.pop()
            return True
        return False
    
    def redo(self):
        """Redoes the last undone operation"""
        if not self.redo_stack.is_empty():
            self.undo_stack.push(self.text)
            self.text = self.redo_stack.pop()
            return True
        return False
    
    def get_text(self):
        """Returns current text"""
        return self.text
    
    def clear(self):
        """Clears all text and history"""
        self.undo_stack.push(self.text)
        self.text = ""
        self.redo_stack = Stack()


# USAGE EXAMPLES
if __name__ == "__main__":
    print("=" * 50)
    print("TEXT EDITOR WITH UNDO/REDO")
    print("=" * 50)
    
    editor = TextEditor()
    
    editor.write("Hello ")
    print(f"After write 'Hello ': '{editor.get_text()}'")
    
    editor.write("World")
    print(f"After write 'World': '{editor.get_text()}'")
    
    editor.write("!")
    print(f"After write '!': '{editor.get_text()}'")
    
    print("\n--- Undo operations ---")
    editor.undo()
    print(f"After undo: '{editor.get_text()}'")
    
    editor.undo()
    print(f"After undo: '{editor.get_text()}'")
    
    editor.undo()
    print(f"After undo: '{editor.get_text()}'")
    
    print("\n--- Redo operations ---")
    editor.redo()
    print(f"After redo: '{editor.get_text()}'")
    
    editor.redo()
    print(f"After redo: '{editor.get_text()}'")

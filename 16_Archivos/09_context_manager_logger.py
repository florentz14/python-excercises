# context_manager_logger.py
# Context manager using class for file logging

class FileLogger:
    """
    Context manager for logging operations to a file.
    
    Usage:
        with FileLogger('app.log') as logger:
            logger.log("Message here")
    """
    
    def __init__(self, filename):
        """Initialize with the log filename."""
        self.filename = filename
        self.file = None
    
    def __enter__(self):
        """Opens the file when entering the context."""
        self.file = open(self.filename, 'a', encoding='utf-8')
        return self
    
    def log(self, message):
        """Writes a message to the log file."""
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.file.write(f"[{timestamp}] {message}\n")
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Closes the file when exiting the context."""
        if self.file:
            self.file.close()
        # Return False to propagate exceptions
        return False


class Timer:
    """
    Context manager for measuring execution time.
    
    Usage:
        with Timer() as t:
            # code to measure
        print(f"Took {t.elapsed} seconds")
    """
    
    def __init__(self):
        self.start = None
        self.end = None
        self.elapsed = None
    
    def __enter__(self):
        import time
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        self.elapsed = self.end - self.start
        return False


# Example usage
if __name__ == "__main__":
    import os
    
    print("=== Context Manager Demo ===\n")
    
    # Example 1: FileLogger
    print("1. FileLogger context manager:")
    log_file = "demo_app.log"
    
    with FileLogger(log_file) as logger:
        logger.log("Application started")
        logger.log("Processing data...")
        logger.log("Operation completed")
    
    print(f"   Log written to '{log_file}'")
    
    # Read and display log contents
    print("   Log contents:")
    with open(log_file, 'r') as f:
        for line in f:
            print(f"     {line.strip()}")
    
    # Clean up demo file
    os.remove(log_file)
    print(f"   (Demo file '{log_file}' removed)")
    
    print()
    
    # Example 2: Timer
    print("2. Timer context manager:")
    
    with Timer() as t:
        # Simulate some work
        total = sum(i ** 2 for i in range(100000))
    
    print(f"   Calculation result: {total}")
    print(f"   Time elapsed: {t.elapsed:.4f} seconds")
    
    print()
    
    # Example 3: Nested context managers
    print("3. Nested context managers:")
    log_file2 = "timed_app.log"
    
    with Timer() as timer:
        with FileLogger(log_file2) as logger:
            logger.log("Starting timed operation")
            result = sum(range(1000000))
            logger.log(f"Result: {result}")
            logger.log("Operation finished")
    
    print(f"   Logged and timed in {timer.elapsed:.4f} seconds")
    os.remove(log_file2)

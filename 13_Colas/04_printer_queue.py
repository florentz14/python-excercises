# Printer Queue Simulator

class Queue:
    """Basic queue implementation using list"""
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add item to the rear of the queue"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return item from the front of the queue"""
        return self.items.pop(0) if not self.is_empty() else None
    
    def front(self):
        """Return front item without removing it"""
        return self.items[0] if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)


class PrinterQueue:
    """Simulates a printer queue system"""
    def __init__(self):
        self.queue = Queue()
        self.job_counter = 0
    
    def add_job(self, document_name, pages):
        """Adds a print job to the queue"""
        self.job_counter += 1
        job = {'id': self.job_counter, 'document': document_name, 'pages': pages}
        self.queue.enqueue(job)
        print(f"Job #{job['id']} added: {document_name} ({pages} pages)")
    
    def process_job(self):
        """Processes the next print job"""
        if not self.queue.is_empty():
            job = self.queue.dequeue()
            print(f"Printing Job #{job['id']}: {job['document']} - {job['pages']} pages")
            return job
        else:
            print("No jobs in queue")
            return None
    
    def show_queue(self):
        """Displays all jobs in the queue"""
        if self.queue.is_empty():
            print("Queue is empty")
        else:
            print(f"\nJobs in queue ({self.queue.size()}):")
            for i, job in enumerate(self.queue.items, 1):
                print(f"  {i}. Job #{job['id']}: {job['document']} ({job['pages']} pages)")


# USAGE EXAMPLES
if __name__ == "__main__":
    print("=" * 60)
    print("PRINTER QUEUE SIMULATOR")
    print("=" * 60)
    
    printer = PrinterQueue()
    
    # Add print jobs
    printer.add_job("Report.pdf", 25)
    printer.add_job("Invoice.docx", 3)
    printer.add_job("Presentation.pptx", 15)
    printer.add_job("Photo.jpg", 1)
    
    printer.show_queue()
    
    print("\n--- Processing jobs ---")
    printer.process_job()
    printer.process_job()
    
    printer.show_queue()
    
    print("\n--- Processing remaining jobs ---")
    printer.process_job()
    printer.process_job()
    printer.process_job()  # No more jobs

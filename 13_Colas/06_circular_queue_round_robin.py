# Circular Queue for Round-Robin CPU Scheduling

class CircularQueue:
    """Circular queue implementation for round-robin scheduling"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.count = 0
    
    def is_full(self):
        return self.count == self.capacity
    
    def is_empty(self):
        return self.count == 0
    
    def enqueue(self, item):
        if self.is_full():
            print("Queue is full!")
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.count += 1
        return True
    
    def dequeue(self):
        if self.is_empty():
            return None
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return item
    
    def size(self):
        return self.count


class RoundRobinScheduler:
    """CPU process scheduler using round-robin algorithm"""
    def __init__(self, time_quantum=3):
        self.queue = CircularQueue(10)
        self.time_quantum = time_quantum
        self.completed_processes = []
    
    def add_process(self, process_name, burst_time):
        """Adds a process to the scheduler"""
        process = {'name': process_name, 'remaining_time': burst_time, 'original_time': burst_time}
        if self.queue.enqueue(process):
            print(f"Process '{process_name}' added (burst time: {burst_time})")
    
    def execute_cycle(self):
        """Executes one scheduling cycle"""
        if self.queue.is_empty():
            print("No processes to execute")
            return False
        
        process = self.queue.dequeue()
        if process:
            execution_time = min(self.time_quantum, process['remaining_time'])
            process['remaining_time'] -= execution_time
            
            print(f"Executing '{process['name']}' for {execution_time} units "
                  f"(remaining: {process['remaining_time']})")
            
            if process['remaining_time'] > 0:
                self.queue.enqueue(process)
            else:
                print(f"Process '{process['name']}' completed!")
                self.completed_processes.append(process['name'])
        
        return True
    
    def run_all(self):
        """Runs until all processes are completed"""
        cycle = 0
        while not self.queue.is_empty():
            cycle += 1
            print(f"\n--- Cycle {cycle} ---")
            self.execute_cycle()
        print(f"\nAll processes completed: {self.completed_processes}")


# USAGE EXAMPLES
if __name__ == "__main__":
    print("=" * 60)
    print("ROUND-ROBIN CPU SCHEDULER")
    print("=" * 60)
    
    scheduler = RoundRobinScheduler(time_quantum=3)
    
    # Add processes
    scheduler.add_process("Process_A", 8)
    scheduler.add_process("Process_B", 4)
    scheduler.add_process("Process_C", 6)
    scheduler.add_process("Process_D", 2)
    
    print("\n" + "=" * 60)
    print("Executing all scheduling cycles:")
    print("=" * 60)
    scheduler.run_all()

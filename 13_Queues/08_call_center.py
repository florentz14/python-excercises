# Call Center Queue with Average Wait Time Tracking

import time
from collections import deque
from datetime import datetime


class CallCenterQueue:
    """Call center queue that tracks wait times"""
    def __init__(self):
        self.queue = deque()
        self.total_wait_time = 0
        self.calls_processed = 0
    
    def receive_call(self, caller_name):
        """Receives a new call"""
        call = {
            'caller': caller_name,
            'arrival_time': time.time(),
            'timestamp': datetime.now().strftime("%H:%M:%S")
        }
        self.queue.append(call)
        print(f"[{call['timestamp']}] Call received from {caller_name}")
        print(f"  Position in queue: {len(self.queue)}")
    
    def answer_call(self):
        """Answers the next call in queue"""
        if not self.queue:
            print("No calls waiting")
            return None
        
        call = self.queue.popleft()
        answer_time = time.time()
        wait_time = answer_time - call['arrival_time']
        self.total_wait_time += wait_time
        self.calls_processed += 1
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] Answering call from {call['caller']}")
        print(f"  Wait time: {wait_time:.2f} seconds")
        
        return call
    
    def get_statistics(self):
        """Returns call center statistics"""
        avg_wait = (self.total_wait_time / self.calls_processed 
                   if self.calls_processed > 0 else 0)
        print(f"\n{'=' * 40}")
        print("CALL CENTER STATISTICS")
        print(f"{'=' * 40}")
        print(f"Calls in queue: {len(self.queue)}")
        print(f"Calls processed: {self.calls_processed}")
        print(f"Total wait time: {self.total_wait_time:.2f} seconds")
        print(f"Average wait time: {avg_wait:.2f} seconds")
    
    def show_queue(self):
        """Shows all callers waiting in queue"""
        if not self.queue:
            print("No callers in queue")
        else:
            print(f"\nCallers waiting ({len(self.queue)}):")
            for i, call in enumerate(self.queue, 1):
                wait = time.time() - call['arrival_time']
                print(f"  {i}. {call['caller']} - waiting {wait:.1f}s")


# USAGE EXAMPLES
if __name__ == "__main__":
    print("=" * 60)
    print("CALL CENTER QUEUE SIMULATION")
    print("=" * 60)
    
    call_center = CallCenterQueue()
    
    # Receive calls
    print("\n--- Incoming calls ---")
    call_center.receive_call("Maria Garcia")
    time.sleep(0.5)
    call_center.receive_call("John Smith")
    time.sleep(0.3)
    call_center.receive_call("Carlos Rodriguez")
    time.sleep(0.2)
    call_center.receive_call("Ana Martinez")
    
    call_center.show_queue()
    
    # Answer some calls
    print("\n--- Answering calls ---")
    time.sleep(0.5)
    call_center.answer_call()
    time.sleep(0.3)
    call_center.answer_call()
    
    # More incoming
    print("\n--- More incoming calls ---")
    call_center.receive_call("Pedro Lopez")
    
    call_center.show_queue()
    
    # Answer remaining
    print("\n--- Answering remaining calls ---")
    time.sleep(0.2)
    call_center.answer_call()
    call_center.answer_call()
    call_center.answer_call()
    
    # Statistics
    call_center.get_statistics()

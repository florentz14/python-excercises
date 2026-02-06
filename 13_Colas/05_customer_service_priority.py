# Customer Service Queue with Priority (VIP and Regular)

from collections import deque


class CustomerServiceQueue:
    """Customer service queue with regular and VIP queues"""
    def __init__(self):
        self.vip_queue = deque()
        self.regular_queue = deque()
        self.ticket_number = 0
    
    def add_customer(self, name, is_vip=False):
        """Adds a customer to the appropriate queue"""
        self.ticket_number += 1
        customer = {'ticket': self.ticket_number, 'name': name, 'vip': is_vip}
        
        if is_vip:
            self.vip_queue.append(customer)
            print(f"VIP Customer #{customer['ticket']}: {name} added")
        else:
            self.regular_queue.append(customer)
            print(f"Customer #{customer['ticket']}: {name} added")
    
    def serve_next(self):
        """Serves the next customer (VIP priority)"""
        if self.vip_queue:
            customer = self.vip_queue.popleft()
            print(f"Now serving VIP #{customer['ticket']}: {customer['name']}")
            return customer
        elif self.regular_queue:
            customer = self.regular_queue.popleft()
            print(f"Now serving #{customer['ticket']}: {customer['name']}")
            return customer
        else:
            print("No customers waiting")
            return None
    
    def show_status(self):
        """Shows current queue status"""
        print(f"\n--- Queue Status ---")
        print(f"VIP Queue: {len(self.vip_queue)} customers")
        for c in self.vip_queue:
            print(f"  - #{c['ticket']}: {c['name']}")
        print(f"Regular Queue: {len(self.regular_queue)} customers")
        for c in self.regular_queue:
            print(f"  - #{c['ticket']}: {c['name']}")


# USAGE EXAMPLES
if __name__ == "__main__":
    print("=" * 60)
    print("CUSTOMER SERVICE QUEUE WITH PRIORITY")
    print("=" * 60)
    
    service = CustomerServiceQueue()
    
    # Add customers
    service.add_customer("John")
    service.add_customer("Alice", is_vip=True)
    service.add_customer("Bob")
    service.add_customer("Carol", is_vip=True)
    service.add_customer("David")
    service.add_customer("Emma", is_vip=True)
    
    service.show_status()
    
    print("\n--- Serving customers ---")
    service.serve_next()  # VIP first
    service.serve_next()  # VIP
    service.serve_next()  # VIP
    service.serve_next()  # Regular
    service.serve_next()  # Regular
    
    service.show_status()

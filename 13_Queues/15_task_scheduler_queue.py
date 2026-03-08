# -------------------------------------------------
# File Name: 15_task_scheduler_queue.py
# Author: Florentino Báez
# Date: 13_Queues
# Description: Task scheduler with queue. Priority or round-robin scheduling.
# -------------------------------------------------

from collections import deque, Counter


def task_scheduler(tasks: list[str], cooldown: int) -> int:
    """
    LeetCode 621. Minimum intervals to complete all tasks with cooldown.
    Same task cannot run within cooldown slots.
    """
    counts = Counter(tasks)
    max_count = max(counts.values())
    num_max = sum(1 for c in counts.values() if c == max_count)
    # At least: (max_count - 1) * (cooldown + 1) + num_max
    return max(len(tasks), (max_count - 1) * (cooldown + 1) + num_max)


class TaskScheduler:
    """Simple task queue with execution time and cooldown."""

    def __init__(self, cooldown: int = 1):
        self.queue = deque()
        self.cooldown = cooldown
        self.last_run = {}

    def add_task(self, task_id: str, duration: int = 1):
        self.queue.append((task_id, duration))

    def run(self) -> list[str]:
        """Execute tasks respecting cooldown. Returns order of execution."""
        result = []
        time = 0
        while self.queue:
            task_id, duration = self.queue.popleft()
            last = self.last_run.get(task_id, -999)
            if time - last <= self.cooldown:
                wait = self.cooldown - (time - last) + 1
                time += wait
            result.append(task_id)
            self.last_run[task_id] = time
            time += duration
        return result


if __name__ == "__main__":
    print("=== Task Scheduler ===\n")

    tasks = ["A", "A", "A", "B", "B", "B"]
    intervals = task_scheduler(tasks, 2)
    print(f"Tasks {tasks}, cooldown=2 -> min intervals: {intervals}")

    print("\n--- Simple Task Queue ---")
    sched = TaskScheduler(cooldown=1)
    sched.add_task("T1", 2)
    sched.add_task("T1", 1)
    sched.add_task("T2", 1)
    order = sched.run()
    print(f"Execution order: {order}")

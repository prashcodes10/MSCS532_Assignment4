#Priority_Queue

class Job:
    def __init__(self, jid, priority, start_time, due_time):
        self.jid = jid
        self.priority = priority
        self.start_time = start_time
        self.due_time = due_time

    def __repr__(self):
        # A readable string representation of the job is returned
        return f"[Job #{self.jid} | Priority: {self.priority} | Start: {self.start_time} | Due: {self.due_time}]"


class MaxPriorityQueue:
    def __init__(self):
        # The internal list to store the heap is initialized
        self.queue = []

    def insert(self, job):
        # The job is checked before insertion to avoid None values
        if job is None:
            print("Invalid job. Cannot insert.")
            return

        self.queue.append(job)
        i = len(self.queue) - 1
        
        while i > 0:
            parent = (i - 1) // 2
            if self.queue[i].priority > self.queue[parent].priority:
                self.queue[i], self.queue[parent] = self.queue[parent], self.queue[i]
                i = parent
            else:
                break

    def extract_max(self):
        # If the queue is empty, a message is shown
        if not self.queue:
            print("Queue is empty.")
            return None

        # The highest-priority job is removed from the root
        top = self.queue[0]
        self.queue[0] = self.queue[-1]
        self.queue.pop()

        # The heap property is restored by bubbling down
        self._heapify(0)
        return top

    def _heapify(self, i):
        # The children indices are computed
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        # The index of the largest value is determined
        if left < len(self.queue) and self.queue[left].priority > self.queue[largest].priority:
            largest = left
        if right < len(self.queue) and self.queue[right].priority > self.queue[largest].priority:
            largest = right

        # A swap is performed if the heap property is violated
        if largest != i:
            self.queue[i], self.queue[largest] = self.queue[largest], self.queue[i]
            # The process is repeated recursively for the affected subtree
            self._heapify(largest)

    def update_priority(self, job, new_priority):
        # The job is validated before proceeding
        if job is None:
            print("Cannot update priority for a null job.")
            return

        # The priority is updated to the new value
        job.priority = new_priority
        i = self.queue.index(job)

        # The job is bubbled up to maintain the heap structure
        while i > 0:
            parent = (i - 1) // 2
            if self.queue[i].priority > self.queue[parent].priority:
                self.queue[i], self.queue[parent] = self.queue[parent], self.queue[i]
                i = parent
            else:
                break

    def is_empty(self):
        # A boolean indicating whether the queue is empty is returned
        return not self.queue
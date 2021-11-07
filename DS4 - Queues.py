
# FIFO structure

class Queue:

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def enqueue(self, data): # O(1) time
        self.queue.append(data)

    def dequeue(self):
        if self.queue_size():
            data = self.queue[0]
            del self.queue[0]
            return data
        else:
            print("too less data!")
            return

    def peek(self):
        return self.queue[0]

    def queue_size(self):
        return len(self.queue)


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(f"size of queue: {q.queue_size()}")

q.dequeue()
print(f"size of queue: {q.queue_size()}")
q.dequeue()
print(f"size of queue: {q.queue_size()}")
q.dequeue()
print(f"size of queue: {q.queue_size()}")
q.dequeue()
print(f"size of queue: {q.queue_size()}")
q.dequeue()
print(f"size of queue: {q.queue_size()}")
q.dequeue()
print(f"size of queue: {q.queue_size()}")

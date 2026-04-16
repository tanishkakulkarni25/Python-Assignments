#Develop a queue implementation using Python's deque from the collection’s module. 
#Add a method, safe_dequeue(), that removes the front element from the queue.
#If the queue is empty, the method should: Print a message as, "Queue is empty, cannot dequeue."
from collections import deque
class Queue:
    def __init__(self):
        self.items = deque()
    def enqueue(self, item):
        self.items.append(item)
    def safe_dequeue(self):
        if len(self.items) == 0:
            print("Queue is empty, cannot dequeue.")
            return None
        return self.items.popleft()
q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.safe_dequeue())  
print(q.safe_dequeue())   
print(q.safe_dequeue())   
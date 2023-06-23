from queueUsingArr import Queue
from queueUsingLL import Queue as QueueLL

q1 = Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)

while q1.isEmpty() != True:
    print(q1.dequeue())

print("Queue operations in linked list queue")
q2 = QueueLL()
q2.enqueue(1)
q2.enqueue(2)
q2.enqueue(3)
q2.enqueue(4)
q2.enqueue(5)

while q2.isEmpty() != True:
    print(q2.dequeue())

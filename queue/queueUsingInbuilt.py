from queueUsingArr import Queue as QueueArr
from queueUsingLL import Queue as QueueLL
from queueUsingTwoStacks import Queue as QueueStk
import queue

q1 = QueueArr()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)

while q1.isEmpty() != True:
    print(q1.dequeue())

print("Queue operations with linked list queue")
q2 = QueueLL()
q2.enqueue(1)
q2.enqueue(2)
q2.enqueue(3)
q2.enqueue(4)
q2.enqueue(5)

while q2.isEmpty() != True:
    print(q2.dequeue())

'''
    Python provides Queue and LifoQueue class in queue module
    It has function like: put == enqueue
                          get == dequeue
                          empty == isEmpty
'''
print("Queue operations with inbuild queue class")
q3 = queue.Queue()
q3.put(1)
q3.put(2)
q3.put(3)
q3.put(4)
q3.put(5)

while q3.empty() != True:
    print(q3.get())

print("Queue operations with Two Stacks queue")
q4 = QueueStk()
q4.enqueue(1)
q4.enqueue(2)
q4.enqueue(3)
q4.enqueue(4)
q4.enqueue(5)


while q4.isEmpty() != True:
    print(q4.dequeue())



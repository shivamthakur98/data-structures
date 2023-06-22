from queueUsingArr import Queue

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

while q.isEmpty() != True:
    print(q.dequeue())

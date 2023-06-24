from stackUsingArr import Stack
from stackUsingLL import Stack as StackLL
from stackUsingTwoQueues import Stack as StackQ
from queue import Queue

'''
    Stack using Array
'''
print("Stack operation using Array")
stack = Stack()
print(stack.size())
stack.push(1)
stack.push(2)
stack.push(3)

while stack.isEmpty() == False:
    print(stack.pop())

'''
    Stack using Linked List
'''
print("Stack operation using LL")
stack = StackLL()
print(stack.size())
stack.push(1)
stack.push(2)
stack.push(3)

while stack.isEmpty() == False:
    print(stack.pop())

'''
    Stack using Lifo Queue
    Python has default implementation for the Queue's which are FIFO data-structure
    It also offers LIFO Queue which is nothing but stack implementation
'''
print("Stack operation using Python's default stack")
stack = Queue()
stack.put(1)
stack.put(2)
stack.put(3)

while stack.empty() == False:
    print(stack.get())

'''
    Stack using Two Queues
'''
print("Stack operation using queues")
stack = StackQ()
stack.push(1)
stack.push(2)
stack.push(3)

while stack.isEmpty() == False:
    print(stack.pop())



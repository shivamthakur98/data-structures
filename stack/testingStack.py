from stackUsingArr import Stack
from stackUsingLL import Stack as StackLL

print("Stack operation using Array")
stack = Stack()
print(stack.size())
stack.push(1)
stack.push(2)
stack.push(3)

while stack.isEmpty() == False:
    print(stack.pop())

print("Stack operation using LL")
stack = StackLL()
print(stack.size())
stack.push(1)
stack.push(2)
stack.push(3)

while stack.isEmpty() == False:
    print(stack.pop())



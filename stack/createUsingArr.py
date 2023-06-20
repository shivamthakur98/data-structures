'''
    Stack implementation using Arrays
'''
class Stack:
    def __init__(self):
        # array is a instance attribute and is private to class only
        self.__arr = list()

    def push(self, value):
        self.__arr.append(value)

    def pop(self):
        if self.isEmpty() == True:
            return "Stack underflow"
        return self.__arr.pop()

    def top(self):
        return self.__arr[len(self.__arr)-1]

    def size(self) -> int:
        return len(self.__arr)

    def isEmpty(self) -> bool:
        return True if len(self.__arr) == 0 else False

print("Creating stack")
stack = Stack()
print(stack.pop())
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.top())
print(stack.size())
print(stack.isEmpty())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.isEmpty())

'''
    Stack implementation using Arrays
'''
class Stack:
    def __init__(self):
        # array is a instance attribute and is private to class only
        self.__data = []

    def push(self, value):
        self.__data.append(value)

    def pop(self):
        if self.isEmpty() == True:
            return "Stack is empty"
        return self.__data.pop()

    def top(self):
        if self.isEmpty() == True:
            return "Stack is empty"
        return self.__data[len(self.__data)-1]

    def size(self) -> int:
        return len(self.__data)

    def isEmpty(self) -> bool:
        return len(self.__data) == 0



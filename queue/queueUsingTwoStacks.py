class Stack:
    def __init__(self):
        self.__data = []
        self.__count = 0

    def push(self, item):
        self.__data.append(item)
        self.__count += 1

    def pop(self):
        if self.isEmpty() == True:
            return -1
        self.__count -= 1
        return self.__data.pop()

    def top(self):
        if self.isEmpty() == True:
            return -1
        return self.__data[self.__count - 1]

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0

'''
    We can implement queues using Two stacks
    One of the function from Enqueue or Dequeue would be O(n)
    here I am making enqueue as o(n)
'''

class Queue:
    def __init__(self):
        self.__mainStack = Stack()
        self.__emptyStack = Stack()
    
    def enqueue(self, item):
        if self.__mainStack.isEmpty() == True:
            self.__mainStack.push(item)
        else:
            self.__moveItemsToEmptyStack()
            self.__mainStack.push(item)
            self.__moveItemsToMainStack()

    def dequeue(self):
        if self.isEmpty() == True:
            return "queue is empty"
        data = self.__mainStack.pop()
        return data

    def front(self):
        if self.isEmpty() == True:
            return "queue is empty"
        return self.__mainStack.top()


    def size(self):
        return self.__mainStack.size()

    def isEmpty(self):
        return self.__mainStack.isEmpty()

    def __moveItemsToEmptyStack(self):
        if self.isEmpty() == True:
            return
        while self.__mainStack.size() > 0:
            data = self.__mainStack.pop()
            self.__emptyStack.push(data)

    def __moveItemsToMainStack(self):
        if self.__emptyStack.isEmpty() == True:
            return
        while self.__emptyStack.size() > 0:
            data = self.__emptyStack.pop()
            self.__mainStack.push(data)



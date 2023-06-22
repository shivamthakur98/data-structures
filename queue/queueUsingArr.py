'''
    Queue's using Array
    Queue is FIFO Structure
    Operations: All these operations are O(1)
    Enqueue
    Dequeue
    front
    size
    isEmpty
'''
class Queue:
    def __init__(self):
        self.__data = []
        self.__front = 0
        self.__count = 0

    def enqueue(self, item):
        self.__data.append(item)
        self.__count += 1

    def dequeue(self):
        if self.isEmpty() == True:
            return "queue is empty"
        data = self.__data[self.__front]
        self.__count -= 1
        self.__front += 1
        return data

    def front(self):
        if self.isEmpty() == True:
            return "queue is empty"
        return self.__data[self.__front]


    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def enqueue(self, item):
        newNode = Node(item)
        if self.__head == None:
            self.__head = newNode
            self.__tail = newNode
        else:
            self.__tail.next = newNode
            self.__tail = self.__tail.next
        self.__count += 1

    def dequeue(self):
        if self.__head == None:
            return "queue is empty"
        data = self.__head.data
        self.__head = self.__head.next
        self.__count -= 1
        return data

    def front(self):
        return self.__head.data

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0

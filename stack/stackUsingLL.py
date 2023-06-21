class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.__head: Node = None
        self.__size: int = 0

    def push(self, data):
        # create a new node and make it head of the LL
        newNode: Node = Node(data)
        newNode.next = self.__head
        self.__head = newNode
        # increment the size
        self.__size += 1

    def pop(self):
        if self.__size == 0:
            return "Stack is empty"
        popedItem = self.__head.data
        self.__head = self.__head.next
        # decrement the size
        self.__size -= 1
        return popedItem

    def top(self):
        if self.__size == 0:
            return "Stack is empty"
        return self.__head.data

    def size(self):
        return self.__size

    def isEmpty(self):
        return self.__size == 0


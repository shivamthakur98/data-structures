from queue import Queue

'''
    I am using inbuilt queues for this
    Here push operation in O(1)
    But pop and top operation are O(n)
'''
'''
    To access the last element we need to
    first pop the n-1 element
    After that only change the reference of
    the queues
'''
'''
    Due to repopulating the original queue
    my testcases were failing
'''

class Stack:
    def __init__(self):
        # here q1 will be main queue
        self.__q1 = Queue()
        # q2 is helper queue
        self.__q2 = Queue()

    def push(self, item):
        self.__q1.put(item)

    def pop(self):
        if self.isEmpty() == True:
            return "Stack is empty"
        # move the n-1 to empty array
        while self.__q1.qsize() > 1:
            self.__q2.put(self.__q1.get())
        
        # get the data to be returned by poping
        data = self.__q1.get()
        # change the reference
        temp = self.__q1
        self.__q1 = self.__q2
        self.__q2 = temp
        return data


    def top(self):
        if self.isEmpty() == True:
            return "Stack is empty"
        # move the n-1 to empty array
        while self.__q1.qsize() > 1:
            self.__q2.put(self.__q1.get())
        
        # get the data to be returned by poping
        data = self.__q1.get()

        # put the element into the q2
        self.__q2.put(data)
        # change the reference
        temp = self.__q1
        self.__q1 = self.__q2
        self.__q2 = temp
        return data

    def size(self):
        return self.__q1.qsize()

    def isEmpty(self):
        return self.__q1.qsize() == 0

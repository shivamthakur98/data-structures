'''
    Cicular Doubly linked list: it contains reference for the previous node plus tail point to head and visa versa
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def takeInput()->Node:
    datas = [int(el) for el in input().strip().split(" ")]
    head, tail = None, None
    for data in datas:
        if data == -1:
            break
        # create Node from the data
        newNode: Node = Node(data)

        # intializing head and tail
        # if head is already intialized, create links
        if head == None:
            head = newNode
            tail = newNode
        else:
            # need to assign value for the tail aswell
            tail.next = newNode
            newNode.prev = tail
            tail = newNode

    # assign values to tails next and heads previous
    tail.next = head
    head.prev = tail
    #return starting point of the Linked List
    return head

def printLL(head):
    currNode = head
    # following changes are required so that while printing it would not stuck in loop
    print(str(currNode.data) + "<=>", end="")
    currNode = currNode.next

    # ending point should be when we reach the head
    while currNode != head:
        print(str(currNode.data) + "<=>", end="")
        currNode = currNode.next
    print(head.data)

def length(head):
    currNode = head.next
    count = 1
    while currNode != head:
        count += 1
        currNode = currNode.next
    return count

'''
    Insertion in the double linked list
'''
def insert(head, i, data):
    currNode = head
    prevNode = None
    newNode = Node(data)
    pos = 0
    size = length(head)

    while pos <= size:
        if pos == i:
            if prevNode == None:
                newNode.next = currNode
                newNode.prev = currNode.prev
                currNode.prev = newNode
                head = newNode
                # remember to remove the reference of old head from the tail
                head.prev.next = head
                break
            else:
                prevNode.next = newNode
                newNode.prev = prevNode
                newNode.next = currNode
                # incase of the last node don;t assign this because currNode is Null
                currNode.prev = newNode
                break

        pos += 1
        prevNode = currNode
        currNode = currNode.next

    return head

no_of_test_cases = int(input("Enter no. of test-cases: "))

while no_of_test_cases > 0:
    head = takeInput()
    printLL(head)
    print("Enter data to be inserted: ")
    pos = int(input("pos: "))
    data = int(input("data: "))
    newHead = insert(head, pos, data)
    print("New list")
    printLL(newHead)

    no_of_test_cases -= 1

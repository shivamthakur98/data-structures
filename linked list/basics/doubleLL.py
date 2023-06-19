'''
    Doubly linked list: it contains reference for the previous node as well
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

    #return starting point of the Linked List
    return head

def printLL(head):
    currNode = head
    while currNode != None:
        print(str(currNode.data) + "<=>", end="")
        currNode = currNode.next
    print("None")

def length(head):
    currNode = head
    count = 0
    while currNode != None:
        count += 1
        currNode = currNode.next
    return count

'''
    Insertion in the double linked list
    No need of the prev pointer
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
                currNode.prev = newNode
                head = newNode
                break
            else:
                prevNode.next = newNode
                newNode.prev = prevNode
                newNode.next = currNode
                # incase of the last node don;t assign this because currNode is Null
                if currNode != None:
                    currNode.prev = newNode
                break

        pos += 1
        prevNode = currNode
        currNode = currNode.next

    return head

'''
    deletion from the linked list
'''
def delete(head, i):
    if i < 0 or i >= length(head):
        return head
    currNode = head
    pos = 0

    while currNode != None:
        if pos == i:
            if currNode == head:
                head = currNode.next
                head.prev = None
                break
            else:
                currNode.prev.next = currNode.next
                if currNode.next != None:
                    currNode.next.prev = currNode.prev
                break
        pos += 1
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
    print("Enter the element to be deleted: ")
    pos = int(input("pos: "))
    head2 = delete(newHead, pos)
    print("New list")
    printLL(head2)

    no_of_test_cases -= 1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteAtIth(head, i):
    currNode = head
    prevNode = None
    pos = 0
    size = lengthOfLL(head)

    if i < 0 or i >= size:
        return
    
    while pos < i:
        pos += 1
        prevNode = currNode
        currNode = currNode.next

    if prevNode == None:
        head = currNode.next
    else:
        prevNode.next = currNode.next
        currNode.next = None
    
    return head


def insertAtIth(head, i, data):
    currNode = head
    prevNode = None
    pos = 0
    # size of linked list
    size = lengthOfLL(head)
    # iterating through the link list to find ith position
    # After finding the ith position create a new node
    # Change the previous node reference with new node
    # In the new node, add reference of the current node
    # In case if the new node is to be placed in the first
    # position, update the head to new node 
    while pos <= size:
        if pos == i:
            newNode = Node(data)
            if prevNode == None:
                head = newNode
            else:
                prevNode.next = newNode

            newNode.next = currNode
            break
        pos += 1
        prevNode = currNode
        currNode = currNode.next

    # as the position of head is mutuable we need to return it
    return head


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
            tail.next = newNode
            tail = newNode

    #return starting point of the Linked List
    return head

def lengthOfLL(head):
    currNode = head
    size = 0
    while currNode != None:
        size += 1
        currNode = currNode.next
    return size

def printLL(head):
    currNode = head
    while currNode != None:
        print(str(currNode.data) + "->", end="")
        currNode = currNode.next
    print("None")

head = takeInput()
printLL(head)
i = int(input("Insert at position: "))
data = int(input("Data: "))
newHead = insertAtIth(head, i, data)
printLL(newHead)


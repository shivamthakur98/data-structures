class Node:
    def __init__(self, data):
        self.data = data
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

def ithPosition(head, i):
    currNode = head
    # assuming the linked list start from pos 0
    position = 0
    
    while currNode != None:
        if position == i:
            break;
        position += 1
        currNode = currNode.next

    if currNode != None:
        print(currNode.data)

def printLL(head):
    currNode = head
    while currNode != None:
        print(str(currNode.data) + "->", end="")
        currNode = currNode.next
    print("None")

head = takeInput()
i = int(input())
# print the linked list
printLL(head)
print("size: " + str(lengthOfLL(head)))
print("data at " + str(i) + ": ", end = "")
ithPosition(head, i)

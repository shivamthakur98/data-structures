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
            '''
                This is line is added so that circular linked list can be made
                In circular linked list, tails has the reference to the first node
            '''
            tail.next = head

    #return starting point of the Linked List
    return head

def printLL(head):
    currNode = head
    # We are printing a circular linked list, so need to take care while printing
    # or loop will be created
    print(str(currNode.data) + "->", end="")
    currNode = currNode.next
    while currNode != head:
        print(str(currNode.data) + "->", end="")
        currNode = currNode.next
    print(head.data)

def length(head)->int:
    if head == None:
        return 0
    currNode = head
    count = 1
    currNode = currNode.next

    while currNode != head:
        count += 1
        currNode = currNode.next

    return count

'''
    Circular Linked list: inserted and deletion of Nodes
'''

def insert(head, i, data):
    currNode = head
    prevNode = None
    oldHead = head
    newNode = Node(data)
    pos = 0
    size = length(head)
    
    # everything else will be same as the simple LL
    # need to take care of the 2 case, 1st head and 2nd tail
    while pos <= size:
        if pos == i:
            # for head, we will be traversing to the tail to point to head in new loop
            if prevNode == None:
                newNode.next = currNode
                head = newNode
                break
            # if we are adding tail, it should refer to first element
            elif currNode == head:
                prevNode.next = newNode
                newNode.next = head
                break
            else:
                prevNode.next = newNode
                newNode.next = currNode
                break
        pos += 1
        prevNode = currNode
        currNode = currNode.next

    # for head case, we have to iterate to the last element as make it refer to head
    if newNode == head:
        currNode = head.next
        while currNode.next != oldHead:
            currNode = currNode.next
        currNode.next = head

    return head

no_of_test_cases = int(input("Enter no. of test-cases: "))

while no_of_test_cases > 0:
    head = takeInput()
    printLL(head)
    print("Enter element to insert: first position and than data: ")
    pos = int(input("Position: "))
    data = int(input("data :"))
    newHead = insert(head, pos, data)
    print("New list: ")
    printLL(newHead)

    no_of_test_cases -= 1

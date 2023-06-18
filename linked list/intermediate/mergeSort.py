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

def printLL(head):
    currNode = head
    while currNode != None:
        print(str(currNode.data) + "->", end="")
        currNode = currNode.next
    print("None")

def mergeSort(head):
    if head == None or head.next == None:
        return head

    # find the midNode to divide the LL into two parts
    midNode = midPoint(head)
    head1 = head
    head2 = midNode.next
    midNode.next = None

    # call mergeSort on the two parts
    nHead1 = mergeSort(head1)
    nHead2 = mergeSort(head2)

    return merge(nHead1, nHead2)

def midPoint(head):
    if head == None:
        return head

    fastNode = head
    slowNode = head

    while fastNode.next != None and fastNode.next.next != None:
        fastNode = fastNode.next.next
        slowNode = slowNode.next

    return slowNode

def merge(head1, head2):
    if head1 == None:
        return head2

    if head2 == None:
        return head1

    newHead = None
    newTail = None

    while head1 != None and head2 != None:
        if head1.data > head2.data:
            if newHead == None:
                newHead = head2
            if newTail != None:
                newTail.next = head2
            newTail = head2
            head2 = head2.next
        else:
            if newHead == None:
                newHead = head1
            if newTail != None:
                newTail.next = head1
            newTail = head1
            head1 = head1.next

    if head1 != None:
        newTail.next = head1

    if head2 != None:
        newTail.next = head2

    return newHead

no_of_test_cases = int(input("Enter no. of test-cases: "))

while no_of_test_cases > 0:
    head = takeInput()
    printLL(head)
    newHead = mergeSort(head)
    print("List After mergeSort: ")
    printLL(newHead)

    no_of_test_cases -= 1

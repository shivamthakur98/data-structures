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

def reverse(head):
    currNode = head
    prevNode = None

    while currNode != None:
        nextNode = currNode.next
        currNode.next = prevNode
        prevNode = currNode
        currNode = nextNode

    return prevNode

'''
    Following are the 4 approaches to reverse the ll recursively
'''
'''
    Approach 1: simple approach with time complexity of O(n^2)
'''
def reverse1(head, prev):
    if head == None or head.next == None:
        return head

    # Inductive step
    newHead = reverse1(head.next)
    currNode = newHead

    while currNode.next != None:
        currNode = currNode.next

    currNode.next = head
    head.next = None

    return newHead

'''
    Approach 2: We will return head as well as tail 
'''
def reverse2(head, prev):
    if head == None or head.next == None:
        return head

    # Inductive step
    newHead, prevTail = reverse1(head.next)

    prevTail.next = head
    head.next = None

    return newHead

'''
    Approach 3: We can get the tail from the head itself 
'''
def reverse3(head, prev):
    if head == None or head.next == None:
        return head

    # Inductive step
    newHead = reverse1(head.next)

    prevTail = head.next
    prevTail.next = head
    head.next = None

    return newHead


'''
    Approach 4: Following the same approach of iterative solution
'''
def reverse4(head, prev):
    if head == None:
        return head

    if head.next == None:
        head.next = prev
        return head

    # Inductive step
    newNode = head.next
    head.next = prev
    prev = head

    # Induction hypothesis
    return reverse2(newNode, prev)

no_of_test_cases = int(input("Enter no. of test-cases: "))

while no_of_test_cases > 0:
    head = takeInput()
    newHead = reverse(head)
    printLL(newHead)
    print("Above list will be reversed recurrsively:")
    newHead2 = reverse2(newHead, None)
    printLL(newHead2)
    no_of_test_cases -= 1
 

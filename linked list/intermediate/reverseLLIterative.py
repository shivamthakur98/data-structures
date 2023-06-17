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
    Reverse the Singly linked list recursively
    Approach one will be giving n-1 value for recursion to reverse
    and adding head to last. But this is not efficiend
    and this soulution will take O(n) time
    Reccurence Relation: T(n) = T(n-1) + n*k

    Recursively reversing the list in the O(n)
'''
def reverse2(head, prev):
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
 

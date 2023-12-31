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

'''
    To find the mid use Fast pointer and slow pointer approach
    i.e. fast pointer should move 2 times faster than slow
'''
def midPoint(head):
    if head == None:
        return head

    fastNode = head
    slowNode = head

    while fastNode.next != None and fastNode.next.next != None:
        fastNode = fastNode.next.next
        slowNode = slowNode.next

    return slowNode

no_of_test_cases = int(input("Enter no. of test-cases: "))

while no_of_test_cases > 0:
    head = takeInput()
    printLL(head)
    print("mid point of the list is: ", end= "")
    mid = midPoint(head)
    print(mid.data)

    no_of_test_cases -= 1

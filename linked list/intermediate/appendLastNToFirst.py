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
Main Code for the problem starts from here
Time Complexity is O(N)

Also Do note the way we find the last element for the array
if we are given the size of elements to be displaced

My Approach: 
    I first calculated the position of "element of interest"
    element_of_interest = lengthOfLL - n
    after that find, newHead and newTail
'''

def appendLastNtoFirst(head, n):
    if n == 0 or head == None:
        return head

    fast = head
    slow = head
    initialHead = head

    # here we are first iterating the size of element given to us
    for i in range(n):
        fast = fast.next

    # here we are pushing the iterated elements to the last
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next

    # After completing these two iteration, fast will point to last element of the List
    # slow will point the element just before the "element of interest"
    temp = slow.next
    fast.next = initialHead
    slow.next = None
    head = temp

    return head

no_of_test_cases = int(input("Enter no. of test-cases: "))

while no_of_test_cases > 0:
    head = takeInput()
    n = int(input("Enter n: "))
    newHead = appendLastNtoFirst(head, n)
    printLL(newHead)

    no_of_test_cases -= 1

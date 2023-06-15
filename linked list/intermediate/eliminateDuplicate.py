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

def removeDuplicate(head):
    currNode = head
    uniq = head

    while currNode != None:
        if currNode.next == None:
            if currNode != uniq:
                uniq.next = None

        elif currNode.data != currNode.next.data:
            if currNode != uniq:
                uniq.next = currNode.next
            uniq = uniq.next
        currNode = currNode.next

    return head 

no_of_test_cases = int(input("Enter no. of test-cases: "))

while no_of_test_cases > 0:
    head = takeInput()
    printLL(head)
    newHead = removeDuplicate(head)
    printLL(head)
    
    no_of_test_cases -= 1

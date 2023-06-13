# structure for the link list
class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None

# iterating through LinkedList
def printLL(head:LinkedList):
    while head != None:
        print(str(head.data) + "->", end ="")
        head = head.next
    print("None")

# creating linked list through user input
# take space seperated input and stop at "-1"
def takeInput() -> LinkedList:
    # input = list(int(el) for el in input().strip().split(""))
    data = [int(el) for el in input().strip().split(" ")]
    head = None
    tail = None
    # currNode = None
    for currInput in data:
        if currInput == -1:
            break
        newNode = LinkedList(currInput)
        if head == None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode

            # using this approach make the time complexity O(n^2)
            # currNode = head
            # while currNode.next != None:
            #     currNode = currNode.next
            # currNode.next = newNode
    
    # return head of the list
    return head 


nodeA = LinkedList(1)
nodeB = LinkedList(2)
nodeA.next = nodeB
printLL(nodeA)
head: LinkedList = takeInput()
printLL(head)

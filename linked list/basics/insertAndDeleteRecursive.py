class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Deleting the list recursively
# If head is null return Null because we can'nt deletion on Null
def deleteAtIth(head, i):
    if head == None:
        return None

    if i == 0:
        head = head.next
        return head
    
    smallHead = deleteAtIth(head.next, i-1)
    head.next = smallHead
    return head

# Insertion in the list Recursively
# Insertion in the empty list is allowed
def insertAtIth(head, i, data):
   # halt case
   if i < 0:
       return head
    
   # insertion in the empty list is allowed
   # that's why this check comes before head == None
   if i == 0:
       newNode = Node(data)
       newNode.next = head
       return newNode

   # if we enter this condition means position given 
   # is more than the length of list so return 
   if head == None:
       return None

   smallHead = insertAtIth(head.next, i-1, data)
   head.next = smallHead
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
    if head == None:
        return 0
    return 1 + lengthOfLL(head.next) 

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
pos = int(input("Delete at position: "))
newHead = deleteAtIth(head, pos)
printLL(newHead)

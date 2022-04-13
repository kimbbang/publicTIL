"""
2022/04/13 solved

Practice Problem :
Doubly Linked List Head Insert
https://practice.geeksforgeeks.org/problems/doubly-linked-list-head-insert/1
"""
#User function Template for python3

def insertInhead(head,data):
    #code here
    new = Node(data)
    new.prev = None
    new.next = head

    head.prev = new

    return new

################### Better solution #########################################
"""
# Adding a node at the front of the list
def push(self, new_data):
 
    # 1 & 2: Allocate the Node & Put in the data
    new_node = Node(data = new_data)
 
    # 3. Make next of new node as head and previous as NULL
    new_node.next = self.head
    new_node.prev = None
 
    # 4. change prev of head node to new node
    if self.head is not None:
        self.head.prev = new_node
 
    # 5. move the head to point to the new node
    self.head = new_node

Better solution :
Doubly Linked List | Set 1 (Introduction and Insertion)
https://www.geeksforgeeks.org/doubly-linked-list/
"""
################### Better solution #########################################


#{
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class doublyLL:
    def __init__(self):
        self.head=None

    def insert(self,tail,data):
        head=self.head

        node=Node(data)

        if not head:

            self.head=node
            return node

        tail.next=node
        node.prev=tail
        return node

def displayList(head):
    while head:
        print(head.data,end=' ')
        pvs=head
        head=head.next
    print()

    while pvs:
        print(pvs.data,end=' ')
        pvs=pvs.prev


if __name__=='__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        headData=int(input())

        dll=doublyLL()

        tail=None

        for nodeData in arr:
            tail=dll.insert(tail,nodeData)

        dll.head=insertInhead(dll.head,headData)
        displayList(dll.head)
        print()

# } Driver Code Ends
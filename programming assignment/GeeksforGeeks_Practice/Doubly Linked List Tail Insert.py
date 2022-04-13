"""
2022/04/13 solved

Practice Problem :
Doubly Linked List Tail Insert
https://practice.geeksforgeeks.org/problems/doubly-linked-list-tail-insert/1
"""
#User function Template for python3

def insertInTail(head,data):
    #code here
    new = Node(data)
    new.next = None

    tmp = head
    while tmp.next:
        tmp = tmp.next

    tmp.next = new
    new.prev = tmp

    return head

################### Better solution #########################################
"""
def append(self, new_data):
 
        # 1. allocate node 2. put in the data
        new_node = Node(data = new_data)
        last = self.head
 
        # 3. This new node is going to be the
        # last node, so make next of it as NULL
        new_node.next = None
 
        # 4. If the Linked List is empty, then
        #  make the new node as head
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
 
        # 5. Else traverse till the last node
        while (last.next is not None):
            last = last.next
 
        # 6. Change the next of last node
        last.next = new_node
        # 7. Make last node as previous of new node */
        new_node.prev = last

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
        tailData=int(input())

        dll=doublyLL()

        tail=None

        for nodeData in arr:
            tail=dll.insert(tail,nodeData)

        dll.head=insertInTail(dll.head,tailData)
        displayList(dll.head)
        print()

# } Driver Code Ends
"""
2022/04/15 solved

Practice Problem :
Delete Head of Doubly Linked List
https://practice.geeksforgeeks.org/problems/delete-head-of-doubly-linked-list/1
"""
#User function Template for python3

def deleteHead(head):
    #code here
    head = head.next
    head.prev = None
    
    return head

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

        dll=doublyLL()

        tail=None

        for nodeData in arr:
            tail=dll.insert(tail,nodeData)

        dll.head=deleteHead(dll.head)
        displayList(dll.head)
        print()

# } Driver Code Ends
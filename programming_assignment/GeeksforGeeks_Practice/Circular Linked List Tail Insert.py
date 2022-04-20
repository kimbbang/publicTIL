"""
2022/04/18 solved

Practice Problem :
Circular Linked List Tail Insert 
https://practice.geeksforgeeks.org/problems/circular-linked-list-tail-insert/0
"""
#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def insertInTail(head,x):
    #code here
    tmp = head.next
    while tmp:
        
        if tmp.next == head:
            new = Node(x)
            tmp.next = new
            new.next = head
            return head
            
        tmp = tmp.next
        
################## ▼ geeks for geeks Solution ▼ ##################
# Circular Singly Linked List | Insertion
# https://www.geeksforgeeks.org/circular-singly-linked-list-insertion/


        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

# contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node



def displayList(head):
    t=head
    while t.next!=head:
        print(t.data,end=' ')
        t=t.next
    print(t.data,end=' ')



if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        n = int(input())
        arr = [int(x) for x in input().split()]
        data=int(input())

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)
        #making circular
        tail.next=ll.head

        resHead=insertInTail(ll.head,data)
        displayList(resHead)
        print()
# } Driver Code Ends
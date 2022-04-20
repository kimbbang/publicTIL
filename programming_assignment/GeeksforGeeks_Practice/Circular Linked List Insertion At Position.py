"""
2022/04/18 solved

Practice Problem :
Circular Linked List Insertion At Position
https://practice.geeksforgeeks.org/problems/circular-linked-list-insertion-at-position/0
"""
#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def insertAtPosition(head,pos,data):
    #code here
    index = pos
    tmp = head
    while tmp:
        if pos != index and tmp == head:    # pos > linked list lnegth 
            return head                     # return orignal head
            
        index -= 1 
        if index == 0:       # insert
            new = Node(data)
            tmp.next, new.next = new, tmp.next
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
        pos,data=[int(x) for x in input().split()]

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)
        #making circular
        tail.next=ll.head

        insertAtPosition(ll.head,pos,data)
        displayList(ll.head)
        print()
# } Driver Code Ends
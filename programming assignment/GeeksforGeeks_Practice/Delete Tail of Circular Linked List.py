"""
2022/04/18 solved

Practice Problem :
Delete Tail of Circular Linked List
https://practice.geeksforgeeks.org/problems/delete-tail-of-circular-linked-list/0
"""
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def deleteTail(head):
    #code here
    if head.next == None:   # head only -> None
        return None
    if head.next.next == None:  # head > target -> head
        head.next = None
        return head
    
    tmp = head
    while tmp:
        
        if tmp.next.next == head:  # tmp > target > head
            tmp.next = head
            return head
            
        tmp = tmp.next

################## ▼ geeks for geeks Solution ▼ ##################
# Deletion from a Circular Linked List
# https://www.geeksforgeeks.org/deletion-circular-linked-list/






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

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)
        #making circular
        tail.next=ll.head

        deleteTail(ll.head)
        displayList(ll.head)
        print()
# } Driver Code Ends
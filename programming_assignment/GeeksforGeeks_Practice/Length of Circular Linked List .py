"""
2022/04/18 solved

Practice Problem :
Length of Circular Linked List 
https://practice.geeksforgeeks.org/problems/length-of-circular-linked-list/1
"""
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def getLength(head):
    #code here
    count = 1
    tmp = head.next
    while tmp:
        
        if tmp == head:
            return count
        count+= 1
        tmp = tmp.next
    
################## ▼ geeks for geeks Solution ▼ ##################
# Count nodes in Circular linked list
# https://www.geeksforgeeks.org/count-nodes-circular-linked-list/


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

        print(getLength(ll.head))
# } Driver Code Ends
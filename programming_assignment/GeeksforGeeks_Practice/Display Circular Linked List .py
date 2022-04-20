"""
2022/04/18 solved

Practice Problem :
Display Circular Linked List 
https://practice.geeksforgeeks.org/problems/display-circular-linked-list/1
"""
##################### ▼ Author's Solution ▼ #####################
#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def displayList(head):
    #code here
    result = [head.data]
    tmp = head.next
    while tmp:
        
        if tmp == head:
            return result 
        result.append(tmp.data)
        tmp = tmp.next

################## ▼ geeks for geeks Solution ▼ ##################
# Circular Linked List | Set 2 (Traversal)
# https://www.geeksforgeeks.org/circular-linked-list-set-2-traversal/

def printList(self):
  
    temp = self.head
      
    # If linked list is not empty
    if self.head is not None:
        while(True):
           
            # Print nodes till we reach first node again
            print(temp.data, end = " ")
            temp = temp.next
            if (temp == self.head):
                break

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

        a = displayList(ll.head)
        for c in a:
            print(c,end=" ")
        print()
# } Driver Code Ends
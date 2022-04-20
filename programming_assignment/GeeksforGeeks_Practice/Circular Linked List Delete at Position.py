"""
2022/04/18 solved

Practice Problem :
Circular Linked List Delete at Position
https://practice.geeksforgeeks.org/problems/circular-linked-list-delete-at-position/0
"""
#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def deleteAtPosition(head,pos):
    #code here
    index = pos
    tmp = head
    while tmp:
        
        if tmp.next == head:  
            if pos == 1:        # last(tmp) > target(head) > next 
                tmp.next = tmp.next.next    
                return tmp.next
            return head         # pos > linkedlist length -> return original 
        
        if index == 2:
            tmp.next = tmp.next.next 
            return head
        
        index -= 1 
        tmp = tmp.next
    

################## ▼ geeks for geeks Solution ▼ ##################
# Deletion from a Circular Linked List
# https://www.geeksforgeeks.org/deletion-circular-linked-list/

def deleteNode( head, key) :
 
    # If linked list is empty
    if (head == None):
        return
         
    # If the list contains only a single node
    if((head).data == key and (head).next == head):
     
        head = None
     
    last = head
    d = None
     
    # If head is to be deleted
    if((head).data == key) :
         
        # Find the last node of the list
        while(last.next != head):
            last = last.next
             
        # Point last node to the next of head i.e.
        # the second node of the list
        last.next = (head).next
        head = last.next
     
    # Either the node to be deleted is not found
    # or the end of list is not reached
    while(last.next != head and last.next.data != key) :
        last = last.next
 
    # If node to be deleted was found
    if(last.next.data == key) :
        d = last.next
        last.next = d.next
     
    else:
        print("no such keyfound")
     
    return head







#{ 
#  Driver Code Starts
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
        pos=int(input())

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)
        #making circular
        tail.next=ll.head

        resHead=deleteAtPosition(ll.head,pos)
        displayList(resHead)
        print()
# } Driver Code Ends
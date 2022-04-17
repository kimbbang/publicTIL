"""
2022/04/17 solved

Practice Problem :
Reverse a Doubly Linked List
https://practice.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/
"""
#User function Template for python3
'''
class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None
'''

def reverseDLL(head):
    #return head after reversing    
    if head == None:        # 0 Node
        return None
        
    if head.next == None:   # 1 Node
        return head
        
    if head.next.next is None:   # 2 Nodes 
        tmp = head.next
        tmp.prev = None
        tmp.next = head
        head.prev = tmp
        head.next = None
        return tmp
        
    tmp = head.next     # more than 3 Nodes
    while tmp:
        tmp.prev.next, tmp.prev.prev = tmp.prev.prev, tmp.prev.next
            
        if tmp.next == None:
            tmp.next, tmp.prev = tmp.prev, tmp.next
            return tmp
            
        tmp = tmp.next    
        
##################### ▼ Author's Solution ▼ #####################
def reverseDLL(head): 
    temp = None
    current = head 

    while current is not None: 
        temp = current.prev  
        current.prev = current.next  #RV: current
        current.next = temp          #RV: !!! prev and next changed !!!
        current = current.prev 

    if temp is not None: 
        head = temp.prev
    return head        
        
################## ▼ geeks for geeks Solution ▼ ##################
# Reverse a Doubly Linked List
# https://www.geeksforgeeks.org/reverse-a-doubly-linked-list/       

def reverseUsingStacks(self):

    stack = []
    temp = self.head
    while temp is not None:
        stack.append(temp.data)   #RV: !!!
        temp = temp.next

    # Add all the elements in the stack
    # in a sequence to the stack
    temp = self.head
    while temp is not None:
        temp.data = stack.pop()   #RV: !!!
        temp = temp.next
        
    # Popped all the elements and the
    # added in the linked list,
    # in a reversed order.






#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None
  
class DoublyLinkedList: 
    def __init__(self): 
        self.head = None
   
    def push(self, new_data,tail):
        if not self.head:
            self.head=Node(new_data)
            return self.head
        Nnode=Node(new_data)
        Nnode.prev=tail
        tail.next=Nnode
        return Nnode
        
    def printList(self, node): 
        while(node is not None): 
            print (node.data,end=' ') 
            node = node.next
            

            
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        
        
        dll=DoublyLinkedList()
        tail=None
        
        for e in arr:
            tail=dll.push(e,tail)
        
        resHead=reverseDLL(dll.head)
        dll.printList(resHead)
        print()
        
# } Driver Code Ends
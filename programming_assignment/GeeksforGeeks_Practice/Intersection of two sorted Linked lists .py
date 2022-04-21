"""
2022/04/21 solved

Practice Problem :
Intersection of two sorted Linked lists 
https://practice.geeksforgeeks.org/problems/intersection-of-two-sorted-linked-lists/1
"""
#User function Template for python3
''' structure of node:
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
# Input
# 6 5
# 1 2 2 3 4 6
# 2 2 4 6 8

# Output
# 2 4 6 

def findIntersection(head1,head2):
    #return head
    tmp1 = head1
    tmp2 = head2
    
    while tmp1.data != tmp2.data:
        if tmp1.data > tmp2.data:
            tmp2 = tmp2.next
        else :         
            tmp1 = tmp1.next
        
    result = tmp1
    rtmp = result 
    
    while tmp1 is not None and tmp2 is not None :
        
        if rtmp.data == tmp1.data:
            tmp1 = tmp1.next
            continue
        if rtmp.data == tmp2.data:
            tmp2 = tmp2.next
            continue
        
        if tmp1.data == tmp2.data :
            rtmp.next = tmp1
            rtmp = rtmp.next
            tmp1 = tmp1.next
            tmp2 = tmp2.next
        
        elif tmp1.data > tmp2.data:
            tmp2 = tmp2.next
        else :         
            tmp1 = tmp1.next
            
    return result 

##################### ▼ Author's Solution ▼ #####################
# Input
# 6 5
# 1 2 2 3 4 6
# 2 2 4 6 8

# Output
# 2 2 4 6 

def findIntersection(head1,head2):
    p1 = head1
    p2 = head2
    head = None
    tail = None
    
    while p1 and p2:
        if p1.data > p2.data:
            # nodes dont match
            # moving to next node in list with smaller node
            p2 = p2.next
        
        elif p2.data > p1.data:
            # nodes dont match
            # moving to next node in list with smaller node
            p1 = p1.next
        
        else:
            # if nodes match:
            
            if head is None:
                head = tail = Node(p1.data)
                # creating new head for intersection list
            else:
                tail.next = Node(p1.data)
                tail = tail.next
                # appending new node at the end
            
            p1=p1.next
            p2=p2.next
            # moving to next nodes in both lists
    
    return head        
        

################## ▼ geeks for geeks Solution ▼ ##################
# Intersection of two Sorted Linked Lists
# https://www.geeksforgeeks.org/intersection-of-two-sorted-linked-lists/
    
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        
        n1,n2 = [int(x) for x in input().split()]
        arr1 = [int(x) for x in input().split()]
        ll1 = linkedList()
        for i in arr1:
            ll1.insert(i)
        
        arr2 = [int(x) for x in input().split()]
        ll2 = linkedList()
        for i in arr2:
            ll2.insert(i)
        
        result = findIntersection(ll1.head,ll2.head)
        printList(result)
        print()

# } Driver Code Ends



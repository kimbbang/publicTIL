"""
2022/04/21 solved

Practice Problem :
Remove duplicates from an unsorted linked list 
https://practice.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/1
"""
#User function Template for python3
'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None    
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        myset = set()
        myset.add(head.data)
        
        pre = head
        tmp = head.next
        nextnode = None
                         #RV: Do not use tmp(current) and pre(node) separately !
        while tmp:
            if tmp.data in myset:     
                nextnode = tmp.next
            
            else:
                myset.add(tmp.data)
                
                if nextnode is not None:
                    pre.next = nextnode
                    nextnode = None
                    
                else:
                    pre.next = tmp
                
                pre = pre.next
                
            tmp = tmp.next  #RV: DON'T DO THIS 
    
        pre.next = nextnode
        return head  

##################### ▼ Author's Solution ▼ #####################
    def removeDuplicates(self, head):
        
         #using set to store already seen values in list. 
        hash=set() 
    
        #using two pointers one of which stores first node other null.
        curr = head
        prev= None
        
        #traversing over the linked list.
        while curr is not None:
            
            #if data at current node is already present in set, we skip the 
            #current node and store the node next to current in link of prev. 
            if curr.data in hash:
                prev.next = curr.next
                #deleting current node which contains duplicates. 
                del curr
            
            #else we just insert the data at current node in set and update 
            #prev to the current node.
            else:
                hash.add(curr.data)
                prev=curr
                
            #updating current to the next node of prev node.
            curr = prev.next  #RV: HERE !!!! 
        
        return head


################## ▼ geeks for geeks Solution ▼ ##################
# Remove duplicates from an unsorted linked list
# https://www.geeksforgeeks.org/remove-duplicates-from-an-unsorted-linked-list/

# METHOD 1 (Using two loops) 
    def remove_duplicates(self):
 
        ptr1 = None
        ptr2 = None
        dup = None
        ptr1 = self.head
 
        # Pick elements one by one
        while (ptr1 != None and ptr1.next != None):
 
            ptr2 = ptr1
 
            # Compare the picked element with rest
            # of the elements
            while (ptr2.next != None):
 
                # If duplicate then delete it
                if (ptr1.data == ptr2.next.data):
 
                    # Sequence of steps is important here
                    dup = ptr2.next
                    ptr2.next = ptr2.next.next
                else:
                    ptr2 = ptr2.next
 
            ptr1 = ptr1.next

# METHOD 3 (Use Hashing) 

    def removeDuplicates(self, head):
 
        # Base case of empty list or
        # list with only one element
        if self.head is None or self.head.next is None:
            return head
 
        # Hash to store seen values
        hash = set()
 
        current = head
        hash.add(self.head.data)
 
        while current.next is not None:
 
            if current.next.data in hash:
                current.next = current.next.next
            else:
                hash.add(current.next.data)
                current = current.next
 
        return head

        
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    # prints the elements of linked list starting with head
    def printList(self):
        if self.head is None:
            print(' ')
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data,end=" ")
            curr_node=curr_node.next
        print(' ')
    
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)
        a.head = Solution().removeDuplicates(a.head)
        a.printList()
# } Driver Code Ends







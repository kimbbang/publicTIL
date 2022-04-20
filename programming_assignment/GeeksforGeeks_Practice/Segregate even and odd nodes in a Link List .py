"""
2022/04/16 solved

Practice Problem :
Segregate even and odd nodes in a Link List 
https://practice.geeksforgeeks.org/problems/segregate-even-and-odd-nodes-in-a-linked-list5035/1
"""
# User function Template for Python3

# Following is the structure of node 
# class Node:
#     def __init__(self):  
#         self.data = None
#         self.next = None

class Solution:
    def divide(self, N, head):
        # code here
        first_even = node()    #RV: "first_even = None" was enough ! 
        last_even = node()     #RV: then "if first_even == None:" on line 28
        first_odd = node()
        last_odd = node()
        
        tmp = head
        while tmp:
            
            if tmp.data % 2 == 0:
                if first_even.data == None:  # first even
                    first_even = tmp
                    last_even = tmp 
                else:
                    last_even.next = tmp
                    last_even = tmp
            
            else : 
                if first_odd.data == None:  # first odd
                    first_odd = tmp
                    last_odd = tmp 
                else:
                    last_odd.next = tmp
                    last_odd = tmp
                
            tmp = tmp.next
        
        last_odd.next = None
        
        if first_even.data == None: # 1 3 5 
            return first_odd
        
        else : 
                                            # 2 4 6 
            if first_odd.data != None:      # 1 2 3 or 2 3 4 
                last_even.next = first_odd
            
            return first_even

################## ▼ geeks for geeks Solution ▼ ##################
# Segregate even and odd nodes in a Linked List
# https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/

# Method 2 - O(n)
def segregateEvenOdd():
    global head
     
    # Starting node of list having
    # even values.
    evenStart = None
     
    # Ending node of even values list.
    evenEnd = None
     
    # Starting node of odd values list.
    oddStart = None
     
    # Ending node of odd values list.
    oddEnd = None
     
    # Node to traverse the list.
    currNode = head
     
    while(currNode != None):
        val = currNode.data
         
        # If current value is even, add
        # it to even values list.
        if(val % 2 == 0):
            if(evenStart == None):
                evenStart = currNode
                evenEnd = evenStart
            else:
                evenEnd . next = currNode
                evenEnd = evenEnd . next
         
        # If current value is odd, add
        # it to odd values list.
        else:
            if(oddStart == None):
                oddStart = currNode
                oddEnd = oddStart
            else:
                oddEnd . next = currNode
                oddEnd = oddEnd . next
                 
        # Move head pointer one step in
        # forward direction
        currNode = currNode . next
     
    # If either odd list or even list is empty,
    # no change is required as all elements
    # are either even or odd.
    if(oddStart == None or evenStart == None):
        return
     
    # Add odd list after even list.    
    evenEnd . next = oddStart
    oddEnd . next = None
     
    # Modify head pointer to
    # starting of even list.
    head = evenStart
 

# Method 1 - O(n)
def segregateEvenOdd():
 
    global head
    end = head
    prev = None
    curr = head
 
    # Get pointer to last Node
    while (end.next != None):
        end = end.next
 
    new_end = end
 
    # Consider all odd nodes before getting first even node
    while (curr.data % 2 !=0 and curr != end):
         
        new_end.next = curr
        curr = curr.next
        new_end.next.next = None
        new_end = new_end.next
         
    # do following steps only if there is an even node
    if (curr.data % 2 == 0):
         
        head = curr
 
        # now curr points to first even node
        while (curr != end):
             
            if (curr.data % 2 == 0):
                 
                prev = curr
                curr = curr.next
                 
            else:
                 
                # Break the link between prev and curr
                prev.next = curr.next
 
                # Make next of curr as None
                curr.next = None
 
                # Move curr to end
                new_end.next = curr
 
                # Make curr as new end of list
                new_end = curr
 
                # Update curr pointer
                curr = prev.next
             
    # We have to set prev before executing rest of this code
    else:
        prev = curr
 
    if (new_end != end and end.data % 2 != 0):
         
        prev.next = end.next
        end.next = None
        new_end.next = end


        
        
        
        

#{ 
#  Driver Code Starts
# Initial Template for Python3

# Node Class    
class node:
    def __init__(self):
        self.data = None
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.tail = self.head
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            self.tail.next = new_node
            self.tail = self.tail.next

def printlist(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print('')

# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        ob = Solution()
        newhead = ob.divide(n, list1.head)
        printlist(newhead)


# } Driver Code Ends
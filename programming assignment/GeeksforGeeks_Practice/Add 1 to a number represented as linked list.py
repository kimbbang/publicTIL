"""
2022/04/17 solved

Practice Problem :
Add 1 to a number represented as linked list
https://practice.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1/
"""
##################### ▼ Author's Solution ▼ #####################
'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
        
    def reverse(self, head):
        prev = None
        current = head
        next = None
        
        while current is not None:
            next = current.next      
            current.next = prev   
            prev = current       
            current = next    
        return prev        
        
    def addOne(self,head):
        #Returns new head of linked List.
        reversed_head = self.reverse(head)  
        
        share = 0
        tmp = reversed_head
        tmp.data += 1 
        while tmp:            
            now = tmp.data + share
            reminder = now % 10
            share = now // 10
            
            tmp.data = reminder
            
            if tmp.next is None and share != 0:  # 999 -> '1'000
                tmp.next = Node(share)
                break
            
            tmp = tmp.next
            
        result = self.reverse(reversed_head)  
        return result 
            
################## ▼ geeks for geeks Solution ▼ ##################
# Add 1 to a number represented as linked list
# https://www.geeksforgeeks.org/add-1-number-represented-linked-list/
    
    def reverseList(head):
        if not head:
            return
        curNode = head
        prevNode = head
        nextNode = head.next
        curNode.next = None
    
        while(nextNode):
            curNode = nextNode
            nextNode = nextNode.next
            curNode.next = prevNode
            prevNode = curNode
    
        return curNode
    
    # Adds one to a linked lists and return the head
    # node of resultant list
    
    
    def addOne(head):
    
        # Reverse linked list and add one to head
        head = reverseList(head)
        k = head
        carry = 0
        prev = None
        head.data += 1
    
        # update carry for next calculation
        while(head != None) and (head.data > 9 or carry > 0):
            prev = head
            head.data += carry
            carry = head.data // 10
            head.data = head.data % 10
            head = head.next
    
        if carry > 0:
            prev.next = Node(carry)
        # Reverse the modified list
        return reverseList(k)
            
            
            
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

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
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

def PrintList(head):
    while head:
        print(head.data,end='')
        head = head.next

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        
        num = input()
        ll = LinkedList() # create a new linked list 'll1'.
        for digit in num:
            ll.insert(int(digit))  # add to the end of the list
        
        resHead = Solution().addOne(ll.head)
        PrintList(resHead)
        print()


# } Driver Code Ends
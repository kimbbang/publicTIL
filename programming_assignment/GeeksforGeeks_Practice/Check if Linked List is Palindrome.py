"""
2022/04/11 solved

Practice Problem :
Check if Linked List is Palindrome
https://practice.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1
"""
#User function Template for python3
'''
    Your task is to check if given linkedlist
    is a pallindrome or not.
    
    Function Arguments: head (reference to head of the linked list)
    Return Type: boolean , no need to print just return True or False.

    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }

    Contributed By: Nagendra Jha
'''
#Function to check whether the list is palindrome.
class Solution:
    def isPalindrome(self, head):
        #code here
        c1 = []
        c2 = []

        tmp = head
        while tmp :
            c1.append(tmp.data)
            c2.append(tmp.data)
            tmp = tmp.next

        if c1 == c2[::-1]:
            return 1
        return 0

##################### ▼ Author's Solution ▼ #####################

    #Function to reverse a linked list.
    def reverseList(self, temp):  
        current = temp;  
        prevNode = None;  
        nextNode = None;  
          
        while(current != None):  
            nextNode = current.next;  
            current.next = prevNode;  
            prevNode = current;  
            current = nextNode;  
        return prevNode;  
              
    
    
    #Function to return the size of linked list.
    def getSize(self, head):
        count = 0
        curr_node = head
        while curr_node:
            count +=1
            curr_node = curr_node.next
        return count
    
    #Function to check whether the list is palindrome.
    def isPalindrome(self, head):  
        current = head;  
        flag = True;  
        
        #finding number of nodes in the list.  
        s = self.getSize(head)
        mid = (s//2) if(s%2 == 0) else ((s+1)//2);  
          
        #finding the middle node in given singly linked list.  
        for i in range(1, mid):  
            current = current.next;  
              
        #reversing the list after middle node to end. 
        revHead = self.reverseList(current.next);  
          
        #comparing nodes of first half and second half of list.  
        while(head != None and revHead != None):  
            if(head.data != revHead.data):  
                flag = False;  
                break;  
                  
            head = head.next;  
            revHead = revHead.next;  
        
        #returning 1 if list is palindrome else 0.    
        return flag


################## ▼ geeks for geeks Solution ▼ ##################
# Function to check if a singly linked list is palindrome
# https://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/






#{
#  Driver Code Starts
#Initial Template for Python 3
#Contributed by : Nagendra Jha

import atexit
import io
import sys

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

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list

        if Solution().isPalindrome(a.head):
            print(1)
        else:
            print(0)
# } Driver Code Ends
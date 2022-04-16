"""
Count nodes of linked list
https://practice.geeksforgeeks.org/problems/count-nodes-of-linked-list/1

2022/04/09
"""
# User function Template for python3

'''

#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        '''


class Solution:

    # Function to count nodes of a linked list.
    def getCount(self, head_node):
        # code here
        result = 0

        tmp = head_node
        while tmp:
            result += 1
            tmp = tmp.next

        return result

 ##################### ▼ Author's Solution ▼ #####################
   
    #Function to count nodes of a linked list.
    def getCount(self, head_node):
        
        #using a pointer for the linked list.
        curr_node=head_node
        count=0
        
        #using a loop to count nodes until we get null in link part of node.
        while curr_node:
            
            #updating counter.
            count+=1
            #updating pointer to the next node.
            curr_node=curr_node.next
            
        #returning the number of nodes.
        return count






# {
#  Driver Code Starts
# Initial Template for Python 3

import io
import sys


# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked list class

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # append at the end of the list
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = self.tail.next


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList()
        nodes = list(map(int, input().strip().split()))  # list containing nodes
        for x in nodes:
            node = Node(x)  # create a new node
            a.append(node)
        print(Solution().getCount(a.head))
# } Driver Code Ends
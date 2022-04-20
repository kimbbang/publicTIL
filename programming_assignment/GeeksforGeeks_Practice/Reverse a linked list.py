"""
2022/04/11 solved

Practice Problem :
Reverse a linked list
https://practice.geeksforgeeks.org/problems/reverse-a-linked-list/1/
"""
# function Template for python3
"""
# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    # Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        # Get all data
        stack = []

        tmp = head
        while tmp.next:
            stack.append(tmp.data)
            tmp = tmp.next
        stack.append(tmp.data)

        # Make new Linked list
        reversed_stack = stack[::-1]

        new_head = Node(reversed_stack[0])
        tmp2 = new_head

        for i in reversed_stack[1:]:
            tmp2.next = Node(i)
            tmp2 = tmp2.next

        return new_head

##################### ▼ Author's Solution ▼ #####################

    def reverseList(self, head):
        if head is None:
            return None
        
        #taking three pointers to store the current, previous and next nodes.
        prev = None
        current = head
        next = current.next
        
        
        while current is not None:
            #taking the next node as next.
            next = current.next 
            
            #storing the previous node in link part of current node.
            current.next = prev 
            
            #updating prev from previous node to current node.
            prev = current
            
            #updating current node to next node.
            current = next           
        
        return prev



################## ▼ geeks for geeks Solution ▼ ##################
# Reverse a linked list
# https://www.geeksforgeeks.org/reverse-a-linked-list/

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev          # JUST SWAP !! 
            prev = current
            current = next
        self.head = prev






# {
#  Driver Code Starts
# Node Class
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


def printList(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' ')
        tmp = tmp.next
    print()


if __name__ == '__main__':
    for i in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]

        lis = Linked_List()
        for i in arr:
            lis.insert(i)

        newHead = Solution().reverseList(lis.head)
        printList(newHead)

# } Driver Code Ends
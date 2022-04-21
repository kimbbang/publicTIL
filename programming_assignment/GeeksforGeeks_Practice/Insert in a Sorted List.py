"""
2022/04/21 solved

Practice Problem :
Insert in a Sorted List
https://practice.geeksforgeeks.org/problems/insert-in-a-sorted-list/1
"""
#{ 
#Driver Code Starts
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
        self.prev=self.head
    
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.prev = self.head
        else:
            self.prev.next = new_node
            self.prev = self.prev.next

def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


 # } Driver Code Ends
#User function Template for python3

class Solution:
    def sortedInsert(self, head1,key):
        # code here
        # return head of edited linked list
        if head1.data > key:
            new = Node(key)
            new.next = head1 
            return new 
        
        tmp = head1
        while tmp.next :
            if tmp.next.data > key:
                nextnode = tmp.next
                tmp.next = Node(key)
                tmp.next.next = nextnode
                return head1
                
            tmp = tmp.next
        
        tmp.next = Node(key)
        return head1 
            

################## ▼ geeks for geeks Solution ▼ ##################
# Given a linked list which is sorted, how will you insert in sorted way
# https://www.geeksforgeeks.org/given-a-linked-list-which-is-sorted-how-will-you-insert-in-sorted-way/        
        
        


#{ 
#Driver Code Starts.
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        
        a = LinkedList()
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)
        
        key=int(input())
        h=Solution().sortedInsert(a.head,key)
        printList(h)

#} Driver Code Ends
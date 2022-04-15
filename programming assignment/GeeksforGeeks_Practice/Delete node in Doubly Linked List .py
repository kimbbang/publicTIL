"""
2022/04/15 solved

Practice Problem :
Delete node in Doubly Linked List 
https://practice.geeksforgeeks.org/problems/delete-node-in-doubly-linked-list/1
"""
#User function Template for python3
'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
'''
class Solution: 
    def deleteNode(self,head, x): 
        # Code here
        if head == None:
            return None
            
        if x == 1:
            head = head.next
            head.prev = None
            return head

        tmp = head
        while tmp.next.next and x > 2:
            tmp = tmp.next
            x -= 1 
            
        if tmp.next.next:
            tmp.next = tmp.next.next
            tmp.next.prev = tmp
            return head
        else : 
            tmp.next = None
            return head

##################### ▼ Author's Solution ▼ #####################
    def deleteNode(self,head, x):
        # Code here
        node = llist.head      #RV: llist ??
        x-=1
        while x!=0:
            node = node.next
            x-=1
        if head is None or node is None:
            return
        if head==node:
            head=node.next
        if node.next is not  None:          #RV: Decomposition !!  
            node.next.prev = node.prev
        if node.prev is not None:
            node.prev.next = node.next
        del node

##################### ▼ geeksforgeeks Solution ▼ #####################
# Delete a node in a Doubly Linked List
# https://www.geeksforgeeks.org/delete-a-node-in-a-doubly-linked-list/

# import gc
    def deleteNode(self, dele):
            
        # Base Case
        if self.head is None or dele is None:
            return
            
        # If node to be deleted is head node
        if self.head == dele:
            self.head = dele.next

        # Change next only if node to be deleted is NOT
        # the last node
        if dele.next is not None:
            dele.next.prev = dele.prev
        
        # Change prev only if node to be deleted is NOT
        # the first node
        if dele.prev is not None:
            dele.prev.next = dele.next
        # Finally, free the memory occupied by dele
        # Call python garbage collector
        gc.collect()        #RV: remove what I am not going to use anymore 



        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_data):
        new_node = Node(new_data)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            self.tail = self.head
            return
        self.tail.next = new_node
        self.tail.next.prev = self.tail
        self.tail = self.tail.next

    def printList(self, node):
        while (node.next is not None):
            node = node.next
        while node.prev is not None:
            node = node.prev
        while (node is not None):
            print(node.data, end=" ")
            node = node.next
        print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        llist = DoublyLinkedList()
        for e in arr:
            llist.append(e)
        pos = int(input())
        Solution().deleteNode(llist.head, pos)
        llist.printList(llist.head)
# Contributed by: Harshit Sidhwa

                               
# } Driver Code Ends
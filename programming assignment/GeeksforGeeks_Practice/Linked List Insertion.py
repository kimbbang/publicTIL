"""
Linked List Insertion
https://practice.geeksforgeeks.org/problems/linked-list-insertion-1587115620/1#

2022/04/09
"""
'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''


class Solution:
    # Function to insert a node at the beginning of the linked list.
    # kimbbang's
    def insertAtBegining(self, head, x):
        # code here
        new = Node(x)

        if not head:
            new.next = None       #RV: self.next=None DEFAULT ! 
        else:
            new.next = head

        head = new
        return head

##################### ▼ Author's Solution 1 ▼ #####################

    #Function to insert a node at the beginning of the linked list.
    def insertAtBegining(self,head,x):
        
        #storing the new node with data in a pointer.
        temp = Node(x)
        #if the linked list is null we just return the new node.
        if head is None:
            return temp
            
        #else we just add the list head to the link part(next) of new node.
        #the new node gets inserted at beginning and becomes the first node.
        temp.next = head
        
        #returning the linked list.
        return temp




    # Function to insert a node at the end of the linked list.
    # kimbbang's
    def insertAtEnd(self, head, x):
        # code here
        new = Node(x)
        if not head:
            new.next = None     #RV: self.next=None DEFAULT ! 
            head = new
        else:
            tmp = head
            while tmp.next != None:
                tmp = tmp.next
            tmp.next = new

        return head


##################### ▼ Author's Solution 2 ▼ #####################
    
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        temp = Node(x)
        #if the linked list is null we just return the new node.
        if head is None:
            return temp
            
        ptr = head
        #we use a pointer to find the last node of list.
        while ptr.next:
            ptr=ptr.next;
            
        #we add the new node to the link part(next) of last node in the list. 
        #the new node gets inserted at end and becomes the last node.
        ptr.next = temp;
        
        #returning the linked list.
        return head     

################## ▼ geeks for geeks Solution ▼ ##################
# Linked List | Set 2 (Inserting a node)
# https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/




# {
#  Driver Code Starts
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList()

        nodes_info = list(map(int, input().split()))
        for i in range(0, len(nodes_info) - 1, 2):
            if (nodes_info[i + 1] == 0):
                a.head = Solution().insertAtBegining(a.head, nodes_info[i])
            else:
                a.head = Solution().insertAtEnd(a.head, nodes_info[i])
        printList(a.head)

# } Driver Code Ends
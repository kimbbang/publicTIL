"""
2022/04/12 solved

Practice Problem :
Delete Alternate Nodes
https://practice.geeksforgeeks.org/problems/delete-alternate-nodes/1
"""
#User function Template for python3
'''class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  
        self.next = None'''

class Solution:

    def deleteAlt(self, head):
        #add code here
        result = head

        rtmp = result
        tmp = head
        while tmp.next is not None and tmp.next.next is not None:

            tmp = tmp.next.next
            rtmp.next = Node(tmp.data)
            rtmp = rtmp.next

        return result

################### Better solution #########################################
"""
### Method 1 (Iterative) 
# deletes alternate nodes of a list starting with head
def deleteAlt(head):
    if (head == None):
        return
 
    # Initialize prev and node to be deleted
    prev = head
    now = head.next
 
    while (prev != None and now != None):
         
        # Change next link of previous node
        prev.next = now.next
 
        # Free memory
        now = None
 
        # Update prev and node
        prev = prev.next
        if (prev != None):
            now = prev.next


### Method 2 (Recursive) 
# deletes alternate nodes of a list starting with head
def deleteAlt(head):
    if (head == None):
        return
 
    node = head.next
 
    if (node == None):
        return
 
    # Change the next link of head
    head.next = node.next
 
    # free memory allocated for node
    #free(node)
 
    # Recursively call for the new next of head
    deleteAlt(head.next)         
            
Better solution :
Delete alternate nodes of a Linked List
https://www.geeksforgeeks.org/delete-alternate-nodes-of-a-linked-list/
"""
################### Better solution #########################################

#{
#  Driver Code Starts
#Initial Template for Python 3

class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize
        # next as null

if __name__=='__main__':
    t = int(input())
    for i in range(t):

        n = int(input())
        arr = list(map(int, input().strip().split()))
        #head = createList(arr, n)
        head = Node(arr[0])
        temp = head
        for i in range(1,len(arr)):
            temp.next = Node(arr[i])
            temp = temp.next


        ob = Solution()
        ob.deleteAlt(head)

        while head is not None:
            print(head.data,end = " ")
            head = head.next
        print()

        # } Driver Code Ends
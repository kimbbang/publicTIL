"""
2022/04/12 solved

Practice Problem :
Find n/k th node in Linked list
https://practice.geeksforgeeks.org/problems/find-nk-th-node-in-linked-list/1
"""
#User function Template for python3

'''class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data   
        self.next = None
'''

def fractionalNodes(head,k):
    #add code here
    stack = []    #RV: I didn't need a list

    tmp = head
    while tmp :

        stack.append(tmp)
        tmp = tmp.next

    index = len(stack) // k - 1 if len(stack) % k == 0 else len(stack) // k

    return stack[index]

##################### ▼ Author's Solution ▼ #####################

def fractionalNodes(head,k):
        if(k<=0 or head is None):
            return None
        fractionalNodes=None          #RV: store just one ! 
        temp=head
        i=0
        while(temp is not None):
            temp=temp.next
            if(i%k==0):
                if(fractionalNodes is None):
                    fractionalNodes=head
                else:
                    fractionalNodes=fractionalNodes.next
            i=i+1
        return fractionalNodes


################## ▼ geeks for geeks Solution ▼ ##################
# Find the fractional (or n/k – th) node in linked list
# https://www.geeksforgeeks.org/find-fractional-nk-th-node-linked-list/






#{
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize
        # next as null

# Linked List class
class LinkedList:

    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None
    def insert(self, val):
        if self.head == None:
            self.head = Node(val)
        else:
            new_node = Node(val)
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node


    def display(self,node):
        while(node is not None):
            print(node.data,end=" ")
            node=node.next



if __name__=='__main__':
    t = int(input())
    for i in range(t):
        lis = LinkedList()
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k=int(input())
        #head = createList(arr, n)
        for i in range(0,len(arr)):
            lis.insert(arr[i])
        ans=fractionalNodes(lis.head,k)
        print(ans.data)
# } Driver Code Ends
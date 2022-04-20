"""
2022/04/12 solved

Practice Problem :
Check If Circular Linked List
https://practice.geeksforgeeks.org/problems/circular-linked-list/1/
"""
#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None


# your task is to complete this function
# function should return true/false or 1/0
def isCircular(head):
    # Code here
    myset = set()         #RV: I didn't need to use set()

    tmp = head
    while tmp :

        if tmp in myset:
            return 1

        myset.add(tmp)
        tmp = tmp.next

    return 0

##################### ▼ Author's Solution ▼ #####################
def isCircular(head):
    # Code here
    temp = head.next;
    while(temp!=None and temp!=head):
        temp=temp.next;
    return temp==head


################## ▼ geeks for geeks Solution ▼ ##################
# Check if a linked list is Circular Linked List
# https://www.geeksforgeeks.org/check-if-a-linked-list-is-circular-linked-list/

def Circular(head):
    if head==None:
        return True
         
    # Next of head
    node = head.next    #RV: I didn't need to gather all nodes. 
    i = 0               #RV: If one node is same that means it's circular Linked List. 
     
    # This loop would stop in both cases (1) If Circular (2) Not circular
    while((node is not None) and (node is not head)):  
        i = i + 1
        node = node.next
     
    return(node==head)





#{
#  Driver Code Starts
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to prit the linked LinkedList
    def printList(self, node):
        temp = node
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next

    def getHead(self):
        return self.head

    def createLoop(self, n):
        if n == 0:
            return None
        temp = self.head
        ptr = self.head
        cnt = 1
        while (cnt != n):
            ptr = ptr.next
            cnt += 1
        # print ptr.data
        while (temp.next):
            temp = temp.next
        temp.next = ptr

# Driver program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n,isloop = list(map(int, input().strip().split()))
        arr=list(map(int, input().strip().split()))
        lst=LinkedList()
        for i in arr:
            lst.push(i)
        if(isloop):
            lst.createLoop(1)
        if isCircular(lst.getHead()):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa
# } Driver Code Ends
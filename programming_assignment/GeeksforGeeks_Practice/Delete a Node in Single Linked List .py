"""
Delete a Node in Single Linked List
https://practice.geeksforgeeks.org/problems/delete-a-node-in-single-linked-list/1

2022/04/09
"""
# your task is to complete this function
# function should return new head pointer

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''


def delNode(head, k):
    # Code here
    if k == 1:
        head = head.next     #RV: Do NOT store temporary value 
        return head          #RV: just return !! 

    tmp = head
    for i in range(1, k - 1):
        tmp = tmp.next

    nextnode = tmp.next
    tmp.next = nextnode.next
    return head


##################### ▼ Author's Solution ▼ #####################

def delNode(head, k):
    # Code here
    if k == 1:
        return head.next
    temp = head
    cnt = 1
    temp2 = head
    while k != cnt and temp is not None:
        temp2 = temp
        temp = temp.next
        cnt+=1
    temp2.next = temp.next
    del temp         #RV: delete value that I don't use anymore
    return head


################## ▼ geeks for geeks Solution ▼ ##################
# Linked List | Set 3 (Deleting a node)
# https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/

def deleteNode(self, key):
         
        # Store head node
        temp = self.head
 
        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
 
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
 
        # if key was not present in linked list
        if(temp == None):
            return
 
        # Unlink the node from linked list
        prev.next = temp.next
 
        temp = None





# {
#  Driver Code Starts
# Node Class
class node:
    def __init__(self):
        self.data = None
        self.next = None


# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while (temp.next):
                temp = temp.next
            temp.next = new_node


def printlist(head):
    temp = head
    while (temp):
        print(temp.data, end=" ")
        temp = temp.next
    print('')


# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        k = int(input())
        newhead = delNode(list1.head, k)
        printlist(newhead)
# Contributed By: Harshit Sidhwa
# } Driver Code Ends
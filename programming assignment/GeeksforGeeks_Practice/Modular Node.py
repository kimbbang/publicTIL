"""
2022/04/12 solved

Practice Problem :
Modular Node
https://practice.geeksforgeeks.org/problems/modular-node/1
"""
#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
def modularNode(head, k):
    #function should return the modular Node
    #if no such node is present then return -1
    result = None
    index = 1

    tmp = head
    while tmp:

        if index % k == 0:
            result = tmp.data

        index += 1
        tmp = tmp.next

    if result is None:
        return -1
    else:
        return result

################### Better solution #########################################
"""
Better solution :
Find modular node in a linked list
https://www.geeksforgeeks.org/find-modular-node-linked-list/
"""
################### Better solution #########################################



    #{
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node



if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n=int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        k=int(input())
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        print(modularNode(a.head,k))


# } Driver Code Ends
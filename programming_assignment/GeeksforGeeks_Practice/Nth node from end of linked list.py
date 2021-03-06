"""
2022/04/09 solved

Practice Problem :
Nth node from end of linked list
https://practice.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1
"""
# User function Template for python3
'''
    Your task is to return the data stored in
    the nth node from end of linked list.

    Function Arguments: head (reference to head of the list), n (pos of node from end)
    Return Type: Integer or -1 if no such node exits.

    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }
'''
# Function to find the data of nth node from the end of a linked list
def getNthFromLast(head, n):
    # code here
    length = 1
    tmp = head
    while tmp.next:
        length += 1
        tmp = tmp.next

    if length < n:
        return -1

    tmp = head
    for i in range(length - n):
        tmp = tmp.next

    return tmp.data

##################### ▼ Author's Solution ▼ #####################

def getNthFromLast(head,n):
    
    #using two pointers, similar to finding middle element.
    curr_node = head
    nth_node = head

    #traversing first n elements with first pointer.
    while n :
        if n and curr_node == None:
            return -1
        curr_node = curr_node.next
        n-=1

    #now traversing with both pointers and when first pointer gives null 
    #we have got the nth node from end in second pointer since the first 
    #pointer had already traversed n nodes and thus had difference of n 
    #nodes with second pointer.
    while curr_node :
        curr_node = curr_node.next
        nth_node = nth_node.next

    #returning the data of nth node from end.
    return nth_node.data
    

################## ▼ geeks for geeks Solution ▼ ##################
# Program for n’th node from the end of a Linked List
# https://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/

def getNthFromLast(head,n):
    # Getting count of linked list
    data = []
    count = 0
    itr = head
    while itr:                               # One Loop enough !
        count += 1
        data.append(itr.data)
        itr = itr.next
       
    # Returning the Nth node        
    try:
        if n > count:
            return -1
        if data[count - n]:
            return data[count-n]
        else:
            return -1
    except IndexError:
        return -1
    else:
        return -1





# {
#  Driver Code Starts
# Initial Template for Python 3
# Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n, nth_node = map(int, input().strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        print(getNthFromLast(a.head, nth_node))
# } Driver Code Ends
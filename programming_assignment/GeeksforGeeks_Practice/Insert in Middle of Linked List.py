"""
Insert in Middle of Linked List
https://practice.geeksforgeeks.org/problems/insert-in-middle-of-linked-list/1

2022/04/10
"""
# User function Template for python3
'''
    Your task is to insert a new node in 
    the middle of the linked list with
    the given value.

    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }

    Function Arguments: head (head of linked list), node 
    (node to be inserted in middle)
    Return Type: None, just insert the new node at mid.
'''


# Function to insert a node in the middle of the linked list.
def insertInMid(head, node):
    # code here
    length = 0
    tmp = head
    while tmp is not None:
        length += 1
        tmp = tmp.next
    target = length // 2 if length % 2 == 0 else length // 2 + 1

    length = 1
    tmp = head
    while tmp:
        if length == target:
            node.next = tmp.next
            tmp.next = node
            break
        tmp = tmp.next
        length += 1

    return head

##################### ▼ Author's Solution ▼ #####################

def insertInMid(head,new_node):
    
    #we take two pointers one of which moves to next node in each
	#iteration and the other moves two nodes in one iteration.
    slow = head
    fast = head.next
    
    #when fast will reach end, slow will be at the middle point.
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    #we store the next node after slow in link part of the new node.
    new_node.next = slow.next
    #we also store the new node in link part of the slow node.
    slow.next = new_node


################## ▼ geeks for geeks Solution ▼ ##################
# Insert node into the middle of the linked list
# https://www.geeksforgeeks.org/insert-node-middle-linked-list/



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

    # creates a new node with given value and appends it at the end of the
    # linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
        return

    # prints the elements of linked list starting with head
    def printList(self):
        if self.head is None:
            print(' ')
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print(' ')


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList()
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)
        mid_elem = int(input())
        insertInMid(a.head, Node(mid_elem))
        a.printList()
# } Driver Code Ends
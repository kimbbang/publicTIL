"""
Display Linked List
https://practice.geeksforgeeks.org/problems/display-linked-list/1

2022/04/09
"""
# User function Template for python3

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''


def displayList(head):
    # code here
    result = []
    tmp = head

    while tmp:
        result.append(tmp.data)
        tmp = tmp.next

    return result


# {
#  Driver Code Starts
# Initial Template for Python 3

import io
import sys


# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked list class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # append at the end of the list
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = self.tail.next


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList()
        nodes = list(map(int, input().strip().split()))  # list containing nodes
        for x in nodes:
            node = Node(x)  # create a new node
            a.append(node)
        l = displayList(a.head)
        for x in l:
            print(x, end=' ')
        print()
        # } Driver Code Ends
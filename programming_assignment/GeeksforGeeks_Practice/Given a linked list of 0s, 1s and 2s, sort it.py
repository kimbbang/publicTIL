"""
2022/04/22 solved

Practice Problem :
Given a linked list of 0s, 1s and 2s, sort it. 
https://practice.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1/
"""
#User function Template for python3
'''
Your task is to segregate the list of 
0s,1s and 2s.

Function Arguments: head of the original list.
Return Type: head of the new list formed.

{
    # Node Class
    class Node:
        def __init__(self, data):   # data -> value stored in node
            self.data = data
            self.next = None
}
'''
class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        # code here
        counterList = [0, 0, 0]
        tmp = head
        while tmp:
            counterList[tmp.data] += 1
            tmp = tmp.next
        del tmp 

        result = None
        tmp = result
        for index, cnt in enumerate(counterList):
            for _ in range(cnt):
                if result == None:
                    result = Node(index)
                    tmp = result
                else:
                    new = Node(index)
                    tmp.next = new
                    tmp = tmp.next

        return result
        
##################### ▼ Author's Solution ▼ #####################

    def segregate(self, head):
        
        #creating three dummy nodes to point to beginning of three linked lists.
        zeroD =Node(0)
        oneD = Node(1)
        twoD = Node(2)
    
        #initializing current pointers for three lists.
        zero = zeroD
        one = oneD
        two = twoD        
        
        curr_node = head
        #traversing over the list with a pointer.
        while curr_node :
            
            #we check data at current node and store the node in it's
            #respective list and update the link part of that list.
            if curr_node.data == 0:
                zero.next = curr_node
                zero = zero.next
            elif curr_node.data == 1:
                one.next = curr_node
                one = one.next
            else:
                two.next = curr_node
                two =two.next
            curr_node = curr_node.next
        
        #attaching the three lists containing 0s,1s and 2s respectively.
        if oneD.next :
            zero.next = oneD.next
        else:
            zero.next = twoD.next
        one.next = twoD.next
        two.next = None
        
        return zeroD.next        

################## ▼ geeks for geeks Solution ▼ ##################
# Sort a linked list of 0s, 1s and 2s by changing links
# https://www.geeksforgeeks.org/sort-linked-list-0s-1s-2s-changing-links/



#{ 
#  Driver Code Starts
#Initial Template for Python 3
#Contributed by : Nagendra Jha

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
    def __init__(self, data):   # data -> value stored in node
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
        
# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print(' ')

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        printList(Solution().segregate(a.head))
# } Driver Code Ends  
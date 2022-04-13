"""
2022/04/13 solved

Practice Problem :
Is The Doubly Linked List Circular
https://practice.geeksforgeeks.org/problems/is-the-doubly-linked-list-circular/1/
"""
#User function Template for python3

class Solution:
    def isCircular(self, head):
        #code here
        tmp = head.next
        while tmp:
            if head == tmp:
                return 1
            tmp = tmp.next

        return 0

#{
#  Driver Code Starts
#Initial Template for Python 3

# contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class doublyLL:
    def __init__(self):
        self.head = None

    def insert(self, tail, data):
        head = self.head

        node = Node(data)

        if not head:
            self.head = node
            return node

        tail.next = node
        node.prev = tail
        return node

if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n = int(input())
        arr = [int(x) for x in input().split()]
        x=int(input())


        dll = doublyLL()

        tail = None

        for nodeData in arr:
            tail = dll.insert(tail, nodeData)

        if x==1:
            # making circular
            tail.next = dll.head
            dll.head.prev = tail
        ob=Solution()
        print(ob.isCircular(dll.head))

# } Driver Code Ends
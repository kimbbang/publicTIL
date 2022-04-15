"""
2022/04/14 solved

Practice Problem :
Find Middle of Circular Doubly Linked List
https://practice.geeksforgeeks.org/problems/find-middle-of-circular-doubly-linked-list/1
"""
#User function Template for python3

class Solution:
    def findMiddle(self, head):
        #code here

        cnt = 0
        tmp = head.next

        while tmp:

            if tmp == head:   # once circulated

                cnt = cnt // 2

                while cnt > 0:

                    tmp = tmp.next
                    cnt -= 1

                return tmp.data

            cnt += 1 # count length
            tmp = tmp.next


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

        dll = doublyLL()

        tail = None

        for nodeData in arr:
            tail = dll.insert(tail, nodeData)

        # making circular
        tail.next = dll.head
        dll.head.prev = tail

        ob=Solution()
        print(ob.findMiddle(dll.head))




# } Driver Code Ends
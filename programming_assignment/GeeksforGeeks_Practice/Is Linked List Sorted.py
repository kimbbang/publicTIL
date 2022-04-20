"""
Is Linked List Sorted
https://practice.geeksforgeeks.org/problems/is-linked-list-sorted/1/

2022/04/10
"""
# User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''


def isSorted(head):
    # code here
    now = head.data

    if head.next is None:
        return 1

    tmp = head.next
    # detect decreasing or increasing
    while head.data == tmp.data:
        tmp = tmp.next

    # decreasing
    if now >= tmp.data:
        now = tmp.data
        tmp = tmp.next

        while tmp:
            if now < tmp.data:
                return 0
            now = tmp.data
            tmp = tmp.next

    # increasing
    else:
        now = tmp.data
        tmp = tmp.next

        while tmp:
            if now > tmp.data:
                return 0
            now = tmp.data
            tmp = tmp.next

    return 1


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        n = int(input())
        arr = [int(x) for x in input().split()]

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)

        res = isSorted(ll.head)
        print(res)
# } Driver Code Ends
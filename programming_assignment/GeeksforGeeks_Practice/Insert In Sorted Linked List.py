"""
Insert In Sorted Linked List
https://practice.geeksforgeeks.org/problems/insert-in-sorted-linked-list/1

2022/04/10
"""
# User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''


def insertInSorted(head, data):
    # code here

    # insert first
    tmp = head
    if tmp.data >= data:
        newnode = Node(data)
        newnode.next = tmp
        return newnode

    # insert middle
    while tmp.next:

        if tmp.next.data >= data:
            nextnode = tmp.next

            newnode = Node(data)
            tmp.next = newnode
            newnode.next = nextnode

            return head

        tmp = tmp.next

    # insert last
    newnode = Node(data)
    newnode.next = None
    tmp.next = newnode
    return head


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


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        n = int(input())
        arr = [int(x) for x in input().split()]
        data = int(input())
        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)

        res = insertInSorted(ll.head, data)
        printList(res)
        print()
# } Driver Code Ends
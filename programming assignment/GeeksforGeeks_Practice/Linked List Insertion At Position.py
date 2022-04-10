"""
Linked List Insertion At Position
https://practice.geeksforgeeks.org/problems/linked-list-insertion-at-position/1

2022/04/10
"""
# User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''


def insertAtPosition(head, pos, data):
    # code here
    tmp = head

    while pos > 1:
        pos -= 1
        if tmp.next == None:
            return 1
        tmp = tmp.next

    nextnode = tmp.next

    newnode = Node(data)
    newnode.next = nextnode
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
        pos, data = [int(x) for x in input().split()]

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)

        insertAtPosition(ll.head, pos, data)
        printList(ll.head)
        print()
# } Driver Code Ends
"""
Linked List Delete at Position
https://practice.geeksforgeeks.org/problems/linked-list-delete-at-position/1

2022/04/10
"""
# User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''


def deleteAtPosition(head, pos):
    # code here
    tmp = head
    if pos == 1:
        return tmp.next

    while pos > 2:
        pos -= 1
        tmp = tmp.next

    tmp.next = tmp.next.next

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
    tmp = head
    while tmp != None:
        print(tmp.data, end=" ")
        tmp = tmp.next
    print()


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        n = int(input())
        arr = [int(x) for x in input().split()]
        x = int(input())

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)

        res = deleteAtPosition(ll.head, x)
        printList(res)
# } Driver Code Ends
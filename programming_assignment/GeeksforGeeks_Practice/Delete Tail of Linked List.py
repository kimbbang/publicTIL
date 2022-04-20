"""
Delete Tail of Linked List
https://practice.geeksforgeeks.org/problems/delete-tail-of-linked-list/1

2022/04/10
"""
# User function Template for python3

def deleteTail(head):
    # code here
    tmp = head
    while tmp.next.next is not None:
        tmp = tmp.next

    tmp.next = None
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

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)

        res = deleteTail(ll.head)
        printList(res)
        print()
# } Driver Code Ends
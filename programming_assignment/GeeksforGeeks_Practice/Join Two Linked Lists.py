"""
2022/04/11 solved

Practice Problem :
Join Two Linked Lists
https://practice.geeksforgeeks.org/problems/join-two-linked-lists/1
"""
#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def joinTheLists(head1, head2):
    #code here
    tmp = head1
    while tmp.next:
        tmp = tmp.next

    tmp.next = head2
    return head1

#{
#  Driver Code Starts
#Initial Template for Python 3

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
    while(head!=None):
        print(head.data, end=" ")
        head=head.next
    head=tmp
    print()

if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        n = int(input())
        arr = [int(x) for x in input().split()]
        m=int(input())
        brr = [int(x) for x in input().split()]

        ll1 = Llist()
        ll2 = Llist()
        tail1 = None
        tail2 = None

        for nodeData in arr:
            tail1 = ll1.insert(nodeData, tail1)

        for nodeData in brr:
            tail2 = ll2.insert(nodeData, tail2)


        res=joinTheLists(ll1.head,ll2.head)
        printList(res)
# } Driver Code Ends
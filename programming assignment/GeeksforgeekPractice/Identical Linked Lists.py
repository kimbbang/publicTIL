"""
Identical Linked Lists
https://practice.geeksforgeeks.org/problems/identical-linked-lists/1/

2022/04/10
"""
# your task is to complete this function
# function should return true/1 if both
# are identical else return false/0
'''
# Node Class
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

'''


# Function to check whether two linked lists are identical or not.
def areIdentical(head1, head2):
    # Code here
    tmp1 = head1
    tmp2 = head2
    while tmp1:
        if tmp1.data != tmp2.data:
            return False
        tmp1 = tmp1.next
        tmp2 = tmp2.next

    # there is something left in head2
    if tmp2:
        return False
    return True


# {
#  Driver Code Starts
# Node Class
class node:
    def __init__(self, val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = node(val)
        new_node.data = val
        new_node.next = self.head
        self.head = new_node


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head1 = createList(arr, n)
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head2 = createList(arr, n)
        if (areIdentical(head1, head2)):
            print('Identical')
        else:
            print('Not identical')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends
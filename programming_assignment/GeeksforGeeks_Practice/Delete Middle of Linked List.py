"""
2022/04/22 solved

Practice Problem :
Delete Middle of Linked List 
https://practice.geeksforgeeks.org/problems/delete-middle-of-linked-list/1
"""
#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def deleteMid(head):
    '''
    head:  head of given linkedList
    return: head of resultant llist
    '''
    #code here
    if head is None or head.next is None:
        return None
    if head.next.next is None:  #RV: NOT NEED
        head.next = None
        return head
    
    slow = head
    fast = head
    pre = None
    while fast:
        if fast.next is None:   #RV: while fast and fast.next:
            break
        if fast.next.next is None:    #RV: NOT NEED
            pre = pre.next
            slow = slow.next
            break
        
        pre = slow
        slow = slow.next
        fast = fast.next.next
        
    pre.next = slow.next
    
    return head
    
##################### ▼ Author's Solution ▼ #####################
    
def deleteMid(head):
    if head is None or head.next is None:
        return None
    
    prev, slow, fast = None, head, head
    
    while fast and fast.next:
        fast = fast.next.next;
        # fast pointer moves 2 nodes ahead everytime loop is run 
        
        prev = slow;
        # updating prev, prev holds previous value of slow pointer
        
        slow = slow.next;
        # slow pointer moves 1 node ahead everytime loop is run
    
    # since slow pointer was moving at half speed, it points at
    # mid node when fast pointer reaches the end
    prev.next = slow.next; # bypassing mid node
    
    return head;

################## ▼ geeks for geeks Solution ▼ ##################
# Delete middle of linked list
# https://www.geeksforgeeks.org/delete-middle-of-linked-list/




#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
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
    print()

if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):
        n=int(input())
        arr1 = [int(x) for x in input().split()]
        ll = Llist()
        tail = None
        for nodeData in arr1:
            tail = ll.insert(nodeData, tail)

        res=deleteMid(ll.head)
        printList(res)
# } Driver Code Ends







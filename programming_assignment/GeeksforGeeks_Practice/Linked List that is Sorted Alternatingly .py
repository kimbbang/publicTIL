"""
2022/04/19 solved

Practice Problem :
Linked List that is Sorted Alternatingly 
https://practice.geeksforgeeks.org/problems/linked-list-that-is-sorted-alternatingly/1
"""
#User function Template for python3
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
def sort(h1):
    # return head

    plist = list()

    tmp = h1
    while tmp:
        plist.append(tmp.data)
        tmp = tmp.next

    result = None
    sorted_list = sorted(plist)
    for i in sorted_list:
        if result is None:
            new = Node(i)
            result = new
        else:
            new.next = Node(i)
            new = new.next

    return result

################## ▼ geeks for geeks Solution ▼ ##################
# Sort a linked list that is sorted alternating ascending and descending orders?
# https://www.geeksforgeeks.org/how-to-sort-a-linked-list-that-is-sorted-alternating-ascending-and-descending-orders/
    
    
def sort(self):
    # Create 2 dummy nodes and initialise as
    # heads of linked lists
    Ahead = self.Node(0)
    Dhead = self.Node(0)
    # Split the list into lists
    self.splitList(Ahead, Dhead)
    Ahead = Ahead.next
    Dhead = Dhead.next
    # reverse the descending list
    Dhead = self.reverseList(Dhead)
    # merge the 2 linked lists
    self.head = self.mergeList(Ahead, Dhead)

# Function to reverse the linked list
def reverseList(self, Dhead):
    current = Dhead
    prev = None
    while current != None:
        self._next = current.next
        current.next = prev
        prev = current
        current = self._next
    Dhead = prev
    return Dhead

# Function to print linked list
def printList(self):
    temp = self.head
    while temp != None:
        print (temp.data,end=" ")
        temp = temp.next
    print()

# A utility function to merge two sorted linked lists
def mergeList(self, head1, head2):
    # Base cases
    if head1 == None:
        return head2
    if head2 == None:
        return head1
    temp = None
    if head1.data < head2.data:
        temp = head1
        head1.next = self.mergeList(head1.next, head2)
    else:
        temp = head2
        head2.next = self.mergeList(head1, head2.next)
    return temp

# This function alternatively splits a linked list with head
# as head into two:
# For example, 10->20->30->15->40->7 is splitted into 10->30->40
# and 20->15->7
# "Ahead" is reference to head of ascending linked list
# "Dhead" is reference to head of descending linked list
def splitList(self, Ahead, Dhead):
    ascn = Ahead
    dscn = Dhead
    curr = self.head
    # Link alternate nodes
    while curr != None:
        # Link alternate nodes in ascending order
        ascn.next = curr
        ascn = ascn.next
        curr = curr.next
        if curr != None:
            dscn.next = curr
            dscn = dscn.next
            curr = curr.next
    ascn.next = None
    dscn.next = None



#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Llist:
    def __init__(self):
        self.head=None
    
    def insert(self,data,tail):
        node=Node(data)
        
        if not self.head:
            self.head=node
            return node
        
        tail.next=node
        return node
        

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        
        n1=int(input())
        arr1=[int(x) for x in input().split()]
        ll1=Llist()
        tail=None
        for nodeData in arr1:
            tail=ll1.insert(nodeData,tail)
            
            
        resHead=sort(ll1.head)
        printList(resHead)
        print()
        
    
    
# } Driver Code Ends
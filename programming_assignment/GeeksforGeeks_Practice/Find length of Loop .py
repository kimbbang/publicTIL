"""
2022/04/11 solved

Practice Problem :
Find length of Loop
https://practice.geeksforgeeks.org/problems/find-length-of-loop/1/
"""
#User function Template for python3

'''
Structure of node

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
#Function to find the length of a loop in the linked list.
def countNodesinLoop(head):
    #Your code here
    flg = False
    cnt = 0
    start = Node(-1)
    myset = set()     #RV: I didn't need set()

    tmp = head
    while tmp:

        if tmp in myset:

            if not flg :
                start = tmp
                flg = True

            else:
                if start == tmp:
                    return cnt

            cnt += 1

        myset.add(tmp)
        tmp = tmp.next

    return 0

##################### ▼ Author's Solution ▼ #####################

#Function to find the length of a loop in the linked list.
def countNodesinLoop(head):
    
    #using two pointers and moving one pointer(slow) by one node and 
    #another pointer(fast) by two nodes in each iteration.
    fast = head.next
    slow = head
    
    while fast!=slow:
        
        #if the node pointed by first pointer(fast) or the node 
        #next to it is null, then loop is not present so we return 0.
        if fast is None or fast.next is None:
            return 0
        
        fast = fast.next.next
        slow = slow.next
        
    #both pointers now point to the same node in the loop.
    
    size = 1
    fast = fast.next
    
    #we start iterating the loop with first pointer and continue till 
    #both pointers point to same node again.
    while fast!=slow:
        fast = fast.next
        #incrementing the counter.
        size+=1
        
    #returning the length of the loop.
    return size
    

################## ▼ geeks for geeks Solution ▼ ##################
# Find length of loop in linked list
# https://www.geeksforgeeks.org/find-length-of-loop-in-linked-list/

def detectLoop(self):
     
    # if linked list is empty then there is no loop, so return 0
    if self.head is None:
        return 0
     
    # Using Floyd’s Cycle-Finding Algorithm Slow-Fast Pointer Method
    slow = self.head
    fast = self.head
    flag = 0 # to show that both slow and fast
             # are at start of the Linked List
    while(slow and slow.next and fast and
          fast.next and fast.next.next):
        if slow == fast and flag != 0:
             
            # Means loop is confirmed in the Linked List. 
            # Now slow and fast are both at the same node which is part of the loop
            count = 1
            slow = slow.next
            while(slow != fast):
                slow = slow.next
                count += 1
            return count
         
        slow = slow.next
        fast = fast.next.next
        flag = 1
    return 0 # No loop





#{
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    #connects last node to node at position pos from begining.
    def loopHere(self,pos):
        if pos==0:
            return

        walk = self.head
        for i in range(1,pos):
            walk = walk.next

        self.tail.next = walk

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())

        LL = LinkedList()
        for i in input().split():
            LL.insert(int(i))

        LL.loopHere(int(input()))

        print(countNodesinLoop(LL.head))

# } Driver Code Ends
"""
2022/04/13 solved

Practice Problem :
Doubly linked list Insertion at given position
https://practice.geeksforgeeks.org/problems/insert-a-node-in-doubly-linked-list/1
"""
# Your task is to complete this function
# function should add a new node after the pth position
# function shouldn't print or return any data

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

'''
#Function to insert a new node at given position in doubly linked list.
def addNode(head, p, data):
    # Code here
    new = Node(data)
    tmp = head

    while p > 0:
        p -= 1
        tmp = tmp.next

    new.prev = tmp

    next_node = tmp.next
    tmp.next = new
    new.next = next_node

    return head

##################### ▼ Author's Solution ▼ #####################

#Function to insert a new node at given position in doubly linked list.
def addNode(head, p, data):

    temp = head
    
    #using a pointer to traverse the linked list till position given.
    while p!=0:
        temp=temp.next
        p-=1
        
    #creating and storing the new node with data in a pointer.
    n = Node(data)
    
    #if the node next to node at given position is null, we make the next
    #as new node and new node's previous link as this current node.
    if temp.next is None:
        n.prev = temp
        temp.next=  n
        
    else:    
        #storing the next node to current node in link part(next) of new node.
        n.next = temp.next
        
        #storing new node in link part(next) of current node.
        temp.next = n
        
        #storing the new node in previous link part(prev) of the node which 
        #was next to current node initially.
        temp.next.prev = n
        
        #store the current node in previous link part(prev) of new node.
        n.prev = temp


################## ▼ geeks for geeks Solution ▼ ##################
# Doubly Linked List | Set 1 (Introduction and Insertion)
# https://www.geeksforgeeks.org/doubly-linked-list/

def insertAfter(self, prev_node, new_data):

    # 1. check if the given prev_node is NULL
    if prev_node is None:
        print("This node doesn't exist in DLL")
        return

    #2. allocate node  & 3. put in the data
    new_node = Node(data = new_data)

    # 4. Make next of new node as next of prev_node
    new_node.next = prev_node.next

    # 5. Make the next of prev_node as new_node
    prev_node.next = new_node

    # 6. Make prev_node as previous of new_node
    new_node.prev = prev_node

    # 7. Change previous of new_node's next node */
    if new_node.next is not None:
        new_node.next.prev = new_node





#{
#  Driver Code Starts
class Node:
    def __init__(self, data):
        self.data = data


        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, new_data):
        new_node = Node(new_data)
        if(self.head == None):
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        return

    def printList(self, node):
        while(node.next is not None):
            node = node.next
        while node.prev is not None:
            node = node.prev
        while(node is not None):
            print(node.data, end=" ")
            node = node.next
        print()

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = map(int, input().strip().split())
        llist = DoublyLinkedList()
        for e in arr:
            llist.add(e)

        pos,data = map(int, input().strip().split())

        addNode(llist.head, pos, data)
        llist.printList(llist.head)

# } Driver Code Ends
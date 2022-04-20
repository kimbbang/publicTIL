"""
2022/04/19 solved

Practice Problem :
Split Singly Linked List Alternatingly
https://practice.geeksforgeeks.org/problems/split-singly-linked-list-alternatingly/1
"""
#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
'''
These are global variables to store heads of split lists
a --- store head of first list
b --- store head of second list
'''
def alternatingSplitList(head):
    global a,b
    #Your code here
    index = 0
    tmp = head
    while tmp:
        
        if index % 2 == 0:
            new = Node(tmp.data)
            new.next = a
            a = new 
            
        else: 
            new = Node(tmp.data)
            new.next = b
            b = new 
               
        tmp = tmp.next     
        index += 1
            
################## ▼ geeks for geeks Solution ▼ ##################
# Alternating split of a given Singly Linked List | Set 1
# https://www.geeksforgeeks.org/alternating-split-of-a-given-singly-linked-list/
    
    
    

#{ 
#  Driver Code Starts

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printList(head):
    temp = head
    while (temp):
        print(temp.data, end=" ")
        
        temp = temp.next
    print()

a=None
b=None
def append(head,data): 
  
    new_node = Node(data)
    if head is None:
        head=new_node
    else:
        new_node.next=head
        head=new_node
    
    return head
    

if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        
        head=None
        a=None
        b=None
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in (values):
            head=append(head,i)
        alternatingSplitList(head)
         
        if n%2 is 0:
            a,b=b,a #Correcting the nodes
        printList(a)
        printList(b)
        t -= 1

# } Driver Code Ends
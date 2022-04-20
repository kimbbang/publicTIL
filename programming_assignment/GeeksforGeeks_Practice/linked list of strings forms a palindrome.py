"""
2022/04/17 solved

Practice Problem :
linked list of strings forms a palindrome
https://practice.geeksforgeeks.org/problems/linked-list-of-strings-forms-a-palindrome/1
"""
#User function Template for python3
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
def compute(head): 
    #return True/False
    forward = ""
    tmp = head
    while tmp:
        forward += tmp.data
        tmp = tmp.next
        
    backward = forward[::-1]
    return forward == backward 
    
################## ▼ geeks for geeks Solution ▼ ##################
# Check if a linked list of strings forms a palindrome
# https://www.geeksforgeeks.org/check-linked-list-strings-form-palindrome/



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
        
        
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        
        n1=int(input())
        arr1=input().split()
        ll1=Llist()
        tail=None
        for nodeData in arr1:
            tail=ll1.insert(nodeData,tail)
            
            
        if compute(ll1.head):
            print('True')
        else:
            print('False')
        
    
    
# } Driver Code Ends
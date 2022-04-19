"""
2022/04/18 solved

Practice Problem :
Compare two linked lists 
https://practice.geeksforgeeks.org/problems/compare-two-linked-lists/1
"""
#User function Template for python3
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
def compare(head1, head2):
    #return 1/-1/0
    word = ["",""]      #RV: I didn't need to store ! 
    
    tmp1 = head1
    tmp2 = head2
    while tmp1 or tmp2:
        if tmp1:
            word[0] += str(tmp1.data)
            tmp1 = tmp1.next
            
        if tmp2:
            word[1] += str(tmp2.data)
            tmp2 = tmp2.next
        
    if word[0] == word[1]:              # if both strings are same
        return 0
    else:
        sortedWord = sorted(word)
        if sortedWord[0] == word[0]:    # if second is lexicographically greater.
            return -1                   # a b a a > a b a b a
        else:                           # if first is lexicographically greater
            return 1                    # a b a b a > a b a a
        

################## ▼ geeks for geeks Solution ▼ ##################
# Compare two strings represented as linked lists
# https://www.geeksforgeeks.org/compare-two-strings-represented-as-linked-lists/

def compare(list1, list2):
     
    # Traverse both lists. Stop when either end of linked
    # list is reached or current characters don't match
    while(list1 and list2 and list1.c == list2.c):  #RV: Find different part !! 
        list1 = list1.next
        list2 = list2.next
 
    # If both lists are not empty, compare mismatching characters
    if(list1 and list2):        
        return 1 if list1.c > list2.c else -1   #RV: Just compare different part !! 
 
    # If either of the two lists has reached end
    if (list1 and not list2):
        return 1
 
    if (list2 and not list1):
        return -1
    return 0    
    
    
    
    
    

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
        arr1=input().split()
        ll1=Llist()
        tail=None
        for nodeData in arr1:
            tail=ll1.insert(nodeData,tail)
            
            
        n2=int(input())
        arr2=input().split()
        ll2=Llist()
        tail=None
        for nodeData in arr2:
            tail=ll2.insert(nodeData,tail)
        
        
        print(compare(ll1.head,ll2.head))
    
# } Driver Code Ends
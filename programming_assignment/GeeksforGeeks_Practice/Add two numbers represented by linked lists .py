"""
2022/04/17 solved

Practice Problem :
Add two numbers represented by linked lists 
https://practice.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1
"""  
#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        first_list = []
        second_list = []
        
        tmp1 = first
        tmp2 = second
        while tmp1 or tmp2:
            if tmp1:
                first_list.append(tmp1.data)
                tmp1 = tmp1.next
            if tmp2:
                second_list.append(tmp2.data)
                tmp2 = tmp2.next
        del tmp1
        del tmp2
                

        first_list = first_list[::-1]
        second_list = second_list[::-1]
        
        result = None
        share = 0
        for i in range(max(len(first_list), len(second_list))):
            
            val1 = first_list[i] if len(first_list) > i else 0
            val2 = second_list[i] if len(second_list) > i else 0    
            
            now = val1 + val2 + share
            remainder = now % 10
            share = now // 10
            
            if result == None:
                result = Node(remainder)
                
            else:
                temp = result
                result = Node(remainder)
                result.next = temp 
            
        if  share != 0 :
            temp = result
            result = Node(share)
            result.next = temp 
            
        return result
            
##################### ▼ Author's Solution ▼ #####################
            
    def reverse(self, head):
        prev = None
        current = head
        next = None
        
        while current is not None:
            next = current.next      
            current.next = prev   
            prev = current       
            current = next    
        
        return prev
    
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        
        #reversing both lists to simplify addition.
        first = self.reverse(first)  
        second = self.reverse(second)  
        
        sumList = None
        carry = 0
        
        #using a loop till both lists and carry gets exhausted.
        while first is not None or second is not None or carry>0:
            #using a variable to store sum of two digits along with carry.
            newVal = carry
            
            #if nodes are left in any of the lists, we add their data in newVal.
            if first is not None:
                newVal += first.data
            if second is not None:
                newVal += second.data
            
            #updating carry.
            carry = newVal//10
            #using modulus to store only a single digit at that place.
            newVal = newVal%10       
            
            #creating new node which gets connected with other nodes that 
            #we get after calculating sum of respective digits
            newNode = Node(newVal)
            #storing the previously made nodes in the link part of new node.
            newNode.next = sumList
            #making the new node as the first node of all previously made node.
            sumList = newNode
            
            #moving ahead in both lists.
            if first:
                first = first.next    
            if second:
                second= second.next
        
        return sumList        

################## ▼ geeks for geeks Solution ▼ ##################
# Add two numbers represented by linked lists | Set 2
# https://www.cdn.geeksforgeeks.org/sum-of-two-linked-lists/      
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
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

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = Solution().addTwoLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends
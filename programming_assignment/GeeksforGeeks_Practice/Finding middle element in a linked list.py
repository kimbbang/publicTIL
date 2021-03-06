"""
2022/04/09 solved

Practice Problem :
Finding middle element in a linked list
https://practice.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1
"""
# your task is to complete this function

'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''

class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        # Code here
        # return the value stored in the middle node
        if head.next == None:
            return head.data

        tempList = []        #RV: I didn't need a list

        tmp = head
        while tmp.next:
            tempList.append(tmp.data)
            tmp = tmp.next
        tempList.append(tmp.data)

        return tempList[len(tempList) // 2]

##################### ▼ Author's Solution ▼ #####################

    def findMid(self, head):
        if head is None:
            return None
    
        ptr1 = head
        ptr2 = head
        while(ptr2 is not None and ptr2.next is not None):
            ptr1 = ptr1.next
            # this pointer moves 1 nodes ahead everytime loop is run
        
            ptr2 = ptr2.next.next
            # this pointer moves 2 nodes ahead everytime loop is run
        
        return ptr1.data                 #RV: HERE ! 
        # since slow was moving with half speed, it is there at halfway point




################### Better solution #########################################
"""
    def printMiddle(self):
        # Initialize two pointers, one will go one step a time (slow), another two at a time (fast)
        slow = self.head
        fast = self.head
 
        # Iterate till fast's next is null (fast reaches end)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
         
        # return the slow's data, which would be the middle element.
        print("The middle element is ", slow.data)

Better solution :
Find the middle of a given linked list
https://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/
"""
################### Better solution #########################################


# {
#  Driver Code Starts
# Initial Template for Python3

# Node Class
class node:
    def __init__(self):
        self.data = None
        self.next = None


# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.tail = self.head
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            self.tail.next = new_node
            self.tail = self.tail.next


def printlist(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print('')


# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        ob = Solution()
        print(ob.findMid(list1.head))

# } Driver Code Ends
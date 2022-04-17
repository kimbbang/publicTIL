"""
2022/04/17 solved

Practice Problem :
Occurence of an integer in a Linked List
https://practice.geeksforgeeks.org/problems/occurence-of-an-integer-in-a-linked-list/1
"""
"""  
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class Solution:
    def count(self, head, search_for):
        # Code here

        result = 0
        now = head
        while now:
            if now.data == search_for:
                result += 1
            now = now.next
        return result 

################## ▼ geeks for geeks Solution ▼ ##################
# Write a function that counts the number of times a given int occurs in a Linked List
# https://www.geeksforgeeks.org/write-a-function-that-counts-the-number-of-times-a-given-int-occurs-in-a-linked-list/



#{ 
#  Driver Code Starts
# Do not delete this comment
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()


if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = int(input())
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        m = int(input())
        k = Solution().count(llist.head, m)
        print(k)
        t -= 1
# Contributed by:Harshit Sidhwa
# } Driver Code Ends
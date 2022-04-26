"""
2022/04/26 solved

Practice Problem :
Reverse Array Using Stack
https://practice.geeksforgeeks.org/problems/reverse-array-using-stack/1
"""
#User function Template for python3
class Solution:
    def reverseArray(self,n,arr):
        #code here
        for i in range(n//2):            
            arr[i], arr[-(i+1)] = arr[-(i+1)], arr[i]
            

################## ▼ docs.python.org ▼ ##################
# docs.python.org - 5.1. More on Lists
# https://docs.python.org/3/tutorial/datastructures.html

class Solution:
    def reverseArray(self,n,arr):
        #code here
        arr.reverse()
            



#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]

        Solution().reverseArray(n, arr)

        for e in arr:
            print(e,end=' ')
        print()
# } Driver Code Ends


################## ▼ geeks for geeks Solution ▼ ##################
# Python program to reverse a stack
# https://www.geeksforgeeks.org/python-program-to-reverse-a-stack/
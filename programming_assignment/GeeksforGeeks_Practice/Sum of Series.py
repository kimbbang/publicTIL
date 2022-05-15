"""
2022/05/15 solved

Practice Problem :
Sum of Series 
https://practice.geeksforgeeks.org/problems/sum-of-series2811/1
"""
'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
#User function Template for python3
class Solution:

    def seriesSum(self,n):
        # code here
        if (n+1) % 2 == 0:
            return (n * (n+1)//2)
        else:
            return ((n+1) * n//2)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Driver code 
if __name__ == "__main__":         
    tc=int(input())
    while tc > 0:
        n=int(input())
        ob = Solution()
        ans = ob.seriesSum(n)
        print(ans)
        tc=tc-1
# } Driver Code Ends
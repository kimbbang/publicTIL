"""
2022/05/23 solved

Practice Problem :
Swap two numbers 
https://practice.geeksforgeeks.org/problems/swap-two-numbers3844/1
"""
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3
class Solution:
    def get(self, a, b):
        #code here
        return b, a
#{ 
#Driver Code Starts.
if __name__ == "__main__":
    t = int (input ())
    for tc in range (t):
        a,b = map(int,input().strip().split())
        ob = Solution()
        ans=ob.get(a,b)
        print(str(ans[0])+" "+str(ans[1]))
#} Driver Code Ends

##################### ▼ Author's Solution ▼ #####################
# Python3 code to swap using XOR
x = 10
y = 5

# Code to swap 'x' and 'y'
x = x ^ y; # x now becomes 15 (1111)
y = x ^ y; # y becomes 10 (1010)
x = x ^ y; # x becomes 5 (0101)

print ("After Swapping: x = ", x, " y =", y)
# This code is contributed by
# Sumit Sudhakar
"""
2022/05/18 solved

Practice Problem :
Find n-th term of series 1, 3, 6, 10, 15, 21
https://practice.geeksforgeeks.org/problems/find-n-th-term-of-series-1-3-6-10-15-215506/1
"""
class Solution:
    def findNthTerm(self, N):
        # code here 
        return int((2 + N) / 2 * (N - 1) + 1) #RV: Make this simple 

##################### ▼ Author's Solution ▼ #####################

class Solution:
    def findNthTerm(self, N):
        ans = (N*(N+1))//2     # Formula to get nth term of the Series
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.findNthTerm(N))
# } Driver Code Ends
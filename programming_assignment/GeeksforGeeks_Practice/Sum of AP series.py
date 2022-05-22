"""
2022/05/22 solved

Practice Problem :
Sum of AP series
https://practice.geeksforgeeks.org/problems/sum-of-ap-series4512/1
"""
#User function Template for python3
class Solution:
    def sum_of_ap(self, n, a, d):
        # Code here
        return int((2*a + (n-1)*d) / 2 * n)
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n, a, d = input().split()
        n = int(n)
        a = int(a)
        d = int(d)
        ob = Solution();
        ans = ob.sum_of_ap(n, a, d)
        print(ans)
# } Driver Code Ends
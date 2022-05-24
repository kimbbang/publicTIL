"""
2022/05/24 solved

Practice Problem :
Sum of odd and even elements 
https://practice.geeksforgeeks.org/problems/sum-of-odd-and-even-elements3033/1
"""
#User function Template for python3
class Solution:
    def find_sum(self, n):
        # Code here
        return sum(range(1, n+1, 2)), sum(range(2, n+1, 2))

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        ob = Solution();
        ans = ob.find_sum(n)
        for _ in ans:
            print(_, end=" ")
        print()
# } Driver Code Ends
"""
2022/05/21 solved

Practice Problem :
Area of Rectange, Right Angled Triangle and Circle
https://practice.geeksforgeeks.org/problems/area-of-rectange-right-angled-triangle-and-circle2600/1
"""  
#User function Template for python3
class Solution:
    def getAreas(self, L , W , B , H , R):
        # code here
        l = list()
        l.append(int(L * W))
        l.append(int(0.5 * B * H))
        l.append(int(3.14 * R * R))
        
        return l

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        L,W,B,H,R=map(int,input().split())
        
        ob = Solution()
        ptr = ob.getAreas(L,W,B,H,R)
        
        print(ptr[0],ptr[1],ptr[2])
# } Driver Code Ends
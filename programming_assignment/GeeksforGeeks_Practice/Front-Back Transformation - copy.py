"""
2022/04/16 solved

Practice Problem :
Front-Back Transformation - copy
https://practice.geeksforgeeks.org/problems/front-back-transformation1659/1
"""
#User function Template for python3

class Solution:

    def convert(self, s):
        # code here

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        search = alphabet[::-1]
        
        capital_alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
        capital_search = capital_alphabet[::-1]
        
        result = []
        for c in s:
            
            if c.isupper() :
                result.append(capital_search[capital_alphabet.index(c)])
            else:
                result.append(search[alphabet.index(c)])
                
        return "".join(result)
        
##################### ▼ Author's Solution ▼ #####################
#RV: print(ord('A'), ord('Z'), ord('a'), ord('z')) # 65 90 97 122
#RV: print(chr(65), chr(90), chr(97), chr(122))  # A Z a z 

    def convert(self, s):
        ans=''
        for i in s:
            if ord(i) >= ord('a') and ord(i) <= ord('z'):     #RV: lower case
                ans += chr(ord('z') - (ord(i) - ord('a')))
            else:                                             #RV: upper case
                ans += chr(ord('Z') - (ord(i) - ord('A')))
        return ans


        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.convert(s)

        print(ans)
# } Driver Code Ends
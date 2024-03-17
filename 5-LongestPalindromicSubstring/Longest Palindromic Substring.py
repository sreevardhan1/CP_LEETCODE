'''Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.'''

#CODE
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPalindrome=""
        dp=[[0]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i]=True
            longestPalindrome=s[i]

        for i in range(len(s)-1,-1,-1):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    if (j-i==1) or dp[i+1][j-1] is True:
                        dp[i][j]=True
                        if len(longestPalindrome)<len(s[i:j+1]):
                            longestPalindrome=s[i:j+1]
        return longestPalindrome
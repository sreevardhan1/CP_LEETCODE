'''Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome. 

Constraints:
-231 <= x <= 231 - 1'''

#CODE
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        rev=0
        while(x>0):
            rem=x%10
            rev=rev*10+rem
            x=x//10
        if(temp==rev):
            return True
        else:
            return False
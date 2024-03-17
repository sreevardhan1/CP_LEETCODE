'''Given a string s consisting of words and spaces, 
return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 
Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.'''

#CODE
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Approach:1 USing split() method and converting str to list
        '''ns=s.strip()
        str_list=list(ns.split(" "))
        length=len(str_list)
        l=str_list[length-1]
        return len(l)'''

        # Approach:2 Using rfind()
        ns=s.strip() # removing trailing and leading spaces in str
        ind=ns.rfind(" ") # getting the index of last space in str 
        return len(ns[ind+1:]) # returning the last word from letter nxt to space to last and getting its length
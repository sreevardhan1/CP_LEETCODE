'''Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.'''

# CODE
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''n=len(strs)
        if n==0:
            return ""
        if n==1:
            return strs[0]
        
        root=strs[0]
        for i in range(len(root)):
            for word in strs[1:]:
                if i==len(word) or word[i]!=root[i]:
                    return root[0:i]
        return root'''

        # Using Zip() function
        lst=list(zip(*strs))
        print(lst)
        prefix=""
        for i in lst:
            if len(set(i))==1:
                prefix+=i[0]
            else:
                break
        return prefix
'''Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
 
Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9'''

#CODE
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack=[]
        while head:
            stack.append(head.val)
            head=head.next
        i=0
        j=len(stack)-1
        flag=True
        while(i<j):
            if(stack[i]!=stack[j]):
                flag=False
                break
            i+=1
            j-=1
        return flag
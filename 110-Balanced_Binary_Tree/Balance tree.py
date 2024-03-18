'''Given a binary tree, determine if it is height-balanced.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104'''

#CODE
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return (self.Height(root)>=0)
    def Height(self,root: Optional[TreeNode]) -> bool:
        if root is None:return 0
        lh=self.Height(root.left)
        rh=self.Height(root.right)
        if (lh<0 or rh<0 or abs(lh-rh)> 1):
            return -1
        return max(lh,rh)+1
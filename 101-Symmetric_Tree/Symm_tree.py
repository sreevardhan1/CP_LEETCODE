'''Given the root of a binary tree, 
check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
 
Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100'''

#CODE
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mirror(self, A: Optional[TreeNode],B: Optional[TreeNode])->bool:
        if(A==None): return B==None
        if(B==None): return A==None
        if(A.val!=B.val):
            return False
        else:
            return self.mirror(A.left,B.right) and self.mirror(A.right,B.left)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.mirror(root.left,root.right)
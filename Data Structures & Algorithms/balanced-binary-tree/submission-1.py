# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        leftmax, rightmax = self.maxTree(root.left), self.maxTree(root.right)
        if abs(leftmax - rightmax) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def maxTree(self, root:Optional[TreeNode]) -> bool:
        if not root:
            return 0
        return 1 + max(self.maxTree(root.left), self.maxTree(root.right))
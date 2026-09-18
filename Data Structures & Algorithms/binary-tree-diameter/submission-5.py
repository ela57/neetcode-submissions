# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxleft, maxright = self.maxTree(root.left), self.maxTree(root.right)
        diam = maxleft + maxright
        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(diam, sub)
    def maxTree(self,root:Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxTree(root.left), self.maxTree(root.right))
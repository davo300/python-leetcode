# 98. Validate Binary Search Tree

# Difficulty: Medium

from Tree import TreeNode
import collections
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, left, right):
            if not node:
                return True
            
            if not (left < node.val < right):
                return False
            
            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right)
        
        return valid(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    sol = Solution()

    # Build the tree
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)

    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)

    print(sol.isValidBST(root))      
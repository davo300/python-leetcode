# 110. Balanced Binary Tree

# Given a binary tree, determine if it is height-balanced.

# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(n) space, 
# where n is the number of nodes in the tree.

from Tree import TreeNode
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root: return [True, 0]

            left = dfs(root.left)
            right = dfs(root.right)
            
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]

if __name__ == "__main__":
    sol = Solution()

    # Build the tree: root = [3, 9, 20, null, null, 15, 7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))


    print(sol.isBalanced(root))
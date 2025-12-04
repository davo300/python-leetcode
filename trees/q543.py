# 226. Diameter of Binary Tree 
# -> Given the root of a binary tree, return the length of the diameter of the tree.

# Difficulty: Easy

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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        
        def dfs(curr):
            
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            nonlocal res
            res = max(res, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return res
         


if __name__ == "__main__":
    sol = Solution()

    # Build the tree: [1,2,3,4,5]
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3)


    print(sol.diameterOfBinaryTree(root))
# 104. Maximum Depth of a Binary Tree 

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along
# the longest path from the root node down to the farthest leaf node.

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


# recursive solution, there are other ways also but this one has best case of O(log(n)) if tree is balanced.

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

if __name__ == "__main__":
    sol = Solution()

    # Build the tree: [3,9,20, null,null, 15,7]
    root = TreeNode(3)
    root.left = TreeNode(9, TreeNode(None), TreeNode(None))
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    # print the max depth of the tree
    print(sol.maxDepth(root))



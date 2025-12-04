# 100. Same Tree 
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return (self.isSameTree(p.left, q.left) and 
                    self.isSameTree(p.right, q.right))
        else:
            return False


if __name__ == "__main__":
    sol = Solution()

    # Build the trees: p = [1,2,3], q = [1,2,3]
    p_root = TreeNode(1)
    p_root.left = TreeNode(2)
    p_root.right = TreeNode(3)
    
    q_root = TreeNode(1)
    q_root.left = TreeNode(2)
    q_root.right = TreeNode(3)

    print(sol.isSameTree(p_root, q_root))
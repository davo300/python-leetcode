# 230. Kth Smallest Element in a BST

# Recommended Time & Space Complexity
# You should aim for a solution as good or 
# better than O(h) time and O(h) space, where h is the height of the given tree.

from Tree import TreeNode
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right


if __name__ == "__main__":
    sol = Solution()

    k = 3
    # Build the tree
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)

    root.left.right = TreeNode(4)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(1)

    print(sol.kthSmallest(root, k))
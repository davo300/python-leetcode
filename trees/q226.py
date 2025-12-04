# 226. Invert Binary Tree -> Given the root of a binary tree, invert the tree, and return its root.

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


if __name__ == "__main__":
    sol = Solution()

    # Build the tree: [4,2,7,1,3,6,9]
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(7, TreeNode(6), TreeNode(9))

    # Invert it
    inverted = sol.invertTree(root)

    # Helper function to print BFS
    from collections import deque
    def bfs_print(node):
        if not node:
            return []
        q, res = deque([node]), []
        while q:
            cur = q.popleft()
            if cur:
                res.append(cur.val)
                q.append(cur.left)
                q.append(cur.right)
            else:
                res.append(None)
        return res

    print(bfs_print(inverted))   # ✅ should print [4,7,2,9,6,3,1]

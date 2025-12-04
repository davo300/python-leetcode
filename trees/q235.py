# 235. Lowest Common Ancestor of a Binary Search Tree

# Recommended Time & Space Complexity
# You should aim for a solution as good or 
# better than O(h) time and O(h) space, where h is the height of the given tree.

from Tree import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur

if __name__ == "__main__":
    sol = Solution()

    # Build the tree
    root = TreeNode(2)
    root.left = TreeNode(1)
 

    # Assign p and q as nodes, not integers
    p = root           # Node with value 2
    q = root.left         # Node with value 4

    print(sol.lowestCommonAncestor(root, p, q).val)
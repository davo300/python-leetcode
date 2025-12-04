# 199. Count Good Nodes in Binary Tree

# Difficulty: Medium

# Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree, Biweekly Contest 26

from Tree import TreeNode
import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            if not node:
                return 0
            
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res
        
        return dfs(root, root.val)


if __name__ == "__main__":
    sol = Solution()

    # Build the tree
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)

    root.left.left = TreeNode(3)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)

    print(sol.goodNodes(root))      
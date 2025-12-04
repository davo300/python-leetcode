# 199. Binary Tree Right Side View

# Difficulty: Medium

# Topics: Tree, Depth-first search, Breadth-first Search, Binary Tree

from typing import Optional, List
from Tree import TreeNode
import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])

        while q: 
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            
            if rightSide:
                res.append(rightSide.val)
        
        return res


if __name__ == "__main__":
    sol = Solution()

    # Build the tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    print(sol.rightSideView(root))      # output: [1, 3, 4]
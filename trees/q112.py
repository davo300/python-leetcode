# 112. Path Sum

# Difficulty: Easy


from Tree import TreeNode
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curSum):
            if not node:
                return False
            
            curSum += node.val

            if not node.left and not node.right:
                return curSum == targetSum
            
            return (dfs(node.left, curSum) or 
                    dfs(node.right, curSum))
        
        return dfs(root, 0) 
            
if __name__ == "__main__":
    sol = Solution()
    # root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    # Build the tree

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)

    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)

    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    
    targetSum = 22

    '''root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    targetSum = 5'''


    print(sol.hasPathSum(root, targetSum))
# 572. Subtree of Another Tree

# Topics:
# Tree, Depth-First Search, String Matching, Binary Tree, Hash Function

# Difficulty: Easy

# Recommended Time & Space Complexity

# You should aim for a solution as good or better than O(m * n) time 
# and O(m + n) space, where n and m are the number of nodes 
# in root and subRoot, respectively.


from Tree import TreeNode
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
    
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and 
                    self.sameTree(root.right, subRoot.right))
        
        return False



if __name__ == "__main__":
    sol = Solution()

    # Build the trees: root = [3,4,5,1,2], subRoot = [4,1,2]
    root = TreeNode(3)
    root.left = TreeNode(4, TreeNode(1), TreeNode(2))
    root.right = TreeNode(5)
    
    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)

    print(sol.isSubtree(root, subRoot))
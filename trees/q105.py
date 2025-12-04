# 105. Construct Binary Tree from in-order and pre-order traversal

# Topics:
# Array, Hash Table, Divide and Conquer, Tree, Binary Tree

# This algorithm just uses DFS to check all of the children until null nodes, 
# then it forms the binary tree like the pre-order list

from Tree import TreeNode
from typing import Optional, List
from print_tree import tree_to_list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1:])

        return root


if __name__ == "__main__":
    sol = Solution()

    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
 
    ans = sol.buildTree(preorder, inorder)

    print(tree_to_list(ans))


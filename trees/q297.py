
from Tree import TreeNode
from print_tree import tree_to_list

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root):
        res = []
        
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(res)
    

    # decodes your encoded data to tree.
    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


if __name__ == "__main__":
    ser = Codec()
    deser = Codec()

    # Build the tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    ans = deser.deserialize(ser.serialize(root))    # serialize first, then deserialize second

    print(tree_to_list(ans))


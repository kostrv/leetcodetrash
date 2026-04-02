# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nodes = []

        def collect(node):
            if not node:
                return 
            collect(node.left)
            nodes.append(node.val)
            collect(node.right)
            
        collect(root)

        for i in range(1, len(nodes)):
            if nodes[i] <= nodes[i-1]:
                return False
        return True

        
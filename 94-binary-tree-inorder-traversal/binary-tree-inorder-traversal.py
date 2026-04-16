# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(node):
            if not node: # конечный узел
                return 

            inorder(node.left) # проходимся по левым узлам
            result.append(node.val) # добавляем значения
            inorder(node.right) # проходимся по правым узлам

        inorder(root)
        return result

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def postorder(node):
            if node is None:
                return

            postorder(node.left) # cначала идем до упора влево
            postorder(node.right) # затем идем до упора вправо
            result.append(node.val) # и только потом записываем текущий узел

        postorder(root)
        return result


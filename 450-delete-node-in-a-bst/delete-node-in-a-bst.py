# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Шаг 1: Ищем узел
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # cлучай 1 и 2 дочерних ключей нет или он только один
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # если есть оба ключа
            curr = root.right
            while curr.left: # находим самый минимальный ключ с правой стороны key (он в любом случае будет больше key по определению бд)
                curr = curr.left

            root.val = curr.val # меняем их местами
            root.right = self.deleteNode(root.right, curr.val) # удаляем преемника из правого поддерева
        
        return root

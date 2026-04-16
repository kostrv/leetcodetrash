# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nodes = []

        def collect(node): # для начала соберем бинарное дерево в массив
            if not node:
                return 

            # проходимся по дереву и собираем ключи
            collect(node.left) 
            nodes.append(node.val)
            collect(node.right)
            
        collect(root)

        # по свойству бинарного дерева, массив должен получиться отсортированный
        for i in range(1, len(nodes)):
            if nodes[i] <= nodes[i-1]: # предыдущий элемент должен быть меньше текущего, иначе структура неверная
                return False
        return True

        
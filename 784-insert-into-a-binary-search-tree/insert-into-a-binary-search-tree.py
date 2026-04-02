
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.last = None

        def insert(node, pos=None):
            if node is None:
                new_node = TreeNode(val)
                if self.last is None:
                    return new_node
                
                if pos == 'right':
                    self.last.right = new_node
                elif pos == 'left':
                    self.last.left = new_node
                return new_node # Возвращаем созданный узел

            self.last = node
            if node.val < val:
                # ТУТ НУЖЕН RETURN, чтобы прокинуть созданный узел наверх
                return insert(node.right, pos='right') 
            else:
                # И ТУТ ТОЖЕ
                return insert(node.left, pos='left')

        # Если дерево пустое, insert вернет новый узел
        # Если не пустое, нам нужно вернуть ИСХОДНЫЙ root
        res = insert(root)
        return root if root else res

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.last = None
        
        def insert(node, pos=None):
            if node is None:
                new_node = TreeNode(val, None, None)
                if self.last is None:
                    # если это самый первый узел, возвращаем его
                    return new_node
                    
                if pos == 'right':
                    self.last.right = new_node
                elif pos == 'left':
                    self.last.left = new_node
                return new_node

            self.last = node
            if node.val < val:
                return insert(node.right, pos='right')
            elif node.val > val:
                return insert(node.left, pos='left')
            
            return node 

        # если дерево пустое, insert вернет новый узел
        # если не пустое, нам нужно вернуть ИСХОДНЫЙ root
        res = insert(root)
        return root if root else res
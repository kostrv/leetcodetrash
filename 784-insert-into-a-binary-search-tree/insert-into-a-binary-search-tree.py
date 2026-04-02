

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.last = None

        def insert(node, pos=None):
            if node is None: # дошли до конца

                new_node = TreeNode(val) # финальный ключ под вставку
                if self.last is None:
                    # если это самый первый ключ, сразу возвращаем его
                    return new_node
                
                # привязываем к родителю в зависимости от pos
                if pos == 'right':
                    self.last.right = new_node
                elif pos == 'left':
                    self.last.left = new_node
                    
                return new_node
            
            self.last = node # сохраняем ссылку на ключ

            # определяем сторону движения
            if node.val < val: # если значение больше значения ключа, вправо
                insert(node.right, pos='right') # отправляем значение ключа и ориентацию вставки

            elif node.val > val: # если меньше, влево
                insert(node.left, pos='left')
            
            return node # Возвращаем текущий узел дальше по цепочке

        # перезаписываем root результатом функции
        return insert(root)
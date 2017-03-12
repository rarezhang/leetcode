# Definition for a binary tree node.

from collections import deque 

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

         
class Tree:
    """
    class TreeNode(object):
        def __init__(self, x=None):
            self.val = x
            self.left = None
            self.right = None
    """
    
    def __init__(self):
        self.root = None
        
    def add(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._add(val, self.root)
            
    def _add(self, val, node):
        """
        breadth first
        """
        queue = deque()
        queue.append(self.root)
        
        while len(queue) != 0:
            node = queue.popleft()
            if node.left is None:
                node.left = TreeNode(val)
                break
            else:
                queue.append(node.left)
            if node.right is None:
                node.right = TreeNode(val)
                break
            else:
                queue.append(node.right)

        

    
    def print_tree(self):  # todo 
        self._print_tree(self.root)
        
    def breadth_first(self):
        tree = []
        if self.root is None:
            return tree
            
        queue = deque() 
        queue.append(self.root)  # queue.push
        
        while len(queue) != 0:
            level = []
            size = len(queue)
            while size > 0:
                tree_node = queue.popleft()  # queue.dequeue
                if tree_node.left is not None:
                    queue.append(tree_node.left)
                if tree_node.right is not None:
                    queue.append(tree_node.right)
                level.append(tree_node.val)
                size -= 1
                
            tree.append(level)
        return(tree)


'''        
t = Tree()
for i in range(10):
    t.add(i)
r = t.breadth_first()
print(r)    
'''
            
            
            
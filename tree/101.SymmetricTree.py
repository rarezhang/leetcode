"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



# top solution 
# recursive 
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def _isSymmetric(left, right):
            if left is None or right is None:
                return left == right
            elif left.val != right.val:
                return False
            else:
                return _isSymmetric(left.left, right.right) and _isSymmetric(left.right, right.left)                
        
        if root is None:
            return True 
        else:
            return _isSymmetric(root.left, root.right)




# top solution 
# iterative, stack, deep first search
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True 
        
        stack = list()
        if root.left is not None:
            if root.right is None:  # left is not None && right is None 
                return False
            stack.append(root.left)  # stack.push 
            stack.append(root.right)
        elif root.right is not None:  # left is not None && right is not None 
            return False
            
        while len(stack) != 0:
            if len(stack) % 2 != 0:
                return False
            left = stack.pop()
            right = stack.pop()
            if left.val != right.val:
                return False
                
            if left.left is not None:
                if right.right is None:
                    return False
                stack.append(left.left)
                stack.append(right.right)
            elif right.right is not None:
                return False
                
            if left.right is not None:
                if right.left is None:
                    return False
                stack.append(left.right)
                stack.append(right.left)
            elif right.left is not None:
                return False
        return True         

        
# improvement 
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def _isSymmetric(a, b, s):
            """
            :para a: tree node a 
            :para b: tree node b
            :para s: stack 
            """
            if a is not None:
                if b is None: 
                    return False, s
                s.append(a)
                s.append(b)
            elif b is not None: 
                return False, s
            return True, s
            
        # ------------------------------
        if root is None: return True 
            
        # stack = list()        
        result, stack = _isSymmetric(root.left, root.right, [])
        if not result:
            return False
        
        while len(stack) != 0:
            if len(stack) % 2 != 0: 
                return False
                
            left = stack.pop()
            right = stack.pop()
            if left.val != right.val: 
                return False
                
            result, stack = _isSymmetric(left.left, right.right, stack)
            if not result: 
                return False
                
            result, stack = _isSymmetric(left.right, right.left, stack)
            if not result: 
                return False
        return True


# top solution 
# iterative
from collections import deque

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        
        queue = deque()
        queue.append(root.left)
        queue.append(root.right)
        
        while len(queue) != 0:
            left = queue.popleft()  # queue.dequeue 
            right = queue.popleft()
            
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True


        
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        
        stack = [(root.left, root.right)]

        while len(stack) != 0:
            left, right = stack.pop()
            
            if left is None and right is None:
                continue
            elif left is None or right is None:
                return False
            elif left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
        return True

        
        
        
from Tree import Tree

alist = [1,2,2,3,4,4,3]
# alist = [1,2,2,None,3,None,3]

tree = Tree()
for x in alist:
    tree.add(x)
print(tree)

sol = Solution()
r = sol.isSymmetric(tree.root)
print(r)        
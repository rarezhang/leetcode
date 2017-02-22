"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''

# top solution 
# deepth first search 
# recursion
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        '''
        if root == None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        '''
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root is not None else 0

# top solution
# deep-first-search
# iterative        
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
            
        stack = []  # stack  
        value = []  # stack  
            
        stack.append(root)  # push
        value.append(1)  # push
        max_value = 0
        
        while len(stack) != 0:
            tree_node = stack.pop()
            temp = value.pop()
            max_value = max(temp, max_value)
            if tree_node.left is not None:
                stack.append(tree_node.left)  # push
                value.append(temp+1)  # push
            if tree_node.right is not None:
                stack.append(tree_node.right)  # push
                value.append(temp+1)  # push
        return max_value
            


        
            
# top solution        
# Breadth-first-search
# iterative 
# claculate the count of the last level
from collections import deque
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
            
        result = 0
        queue = deque()
        queue.append(root)  # queue.push
        
        while len(queue) != 0:            
            size = len(queue)
            while size > 0:
                tree_node = queue.popleft()
                if tree_node.left is not None:
                    queue.append(tree_node.left)
                if tree_node.right is not None:
                    queue.append(tree_node.right)
                size -= 1
            result += 1    
        return result
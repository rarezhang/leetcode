"""
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:
Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# top solution 
# deep first search 
# recursion
# The solution is correct, but it is also bound to the application stack, which means that it's no so much scalable - (the problem size will overflow the stack and crash your application), so more robust solution would be to use stack data structure.
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(root.left)
            return root 


# top solution 
# stack 
# deep first search 
# iterative 
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """            
        # stack = []
        # stack.append(root)  # push
        stack = [root]
        
        while stack:
            tree_node = stack.pop()
            if tree_node:
                tree_node.left, tree_node.right = tree_node.right, tree_node.left
                stack.append(tree_node.left)
                stack.append(tree_node.right)
        return root     
            
# top solution
# Breadth-first-search
# iterative 
# level order traversal    
from collections import deque    
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        queue = deque()
        queue.append(root)  # enqueue
        
        while len(queue)!=0:
            tree_node = queue.popleft()  # dequeue
            if tree_node:
                tree_node.left, tree_node.right = tree_node.right, tree_node.left
                queue.append(tree_node.left)
                queue.append(tree_node.right)
        return root
"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""

# top solution 
# based on the definition of balanced binary tree
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def depth(node):
            if node is None:
                return 0
            return 1 + max(depth(node.left), depth(node.right))
        # ---------------------------------    
        if root is None:
            return True
        
        left = depth(root.left)
        right = depth(root.right)
        
        return abs(left - right) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
        

        
# top solution 
# DFS. Instead of calling depth() explicitly for each child node, we return the height of the current node in DFS recursion. When the sub tree of the current node (inclusive) is balanced, the function dfsHeight() returns a non-negative value as the height. Otherwise -1 is returned. According to the leftHeight and rightHeight of the two children, the parent node could check if the sub tree is balanced, and decides its return value.        
# bottom up approach, each node in the tree only need to be accessed once. Thus the time complexity is O(N), better than the first solution.
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs_height(node):
            if node is None:
                return 0
            left_height = dfs_height(node.left)
            if left_height == -1:  # once a sub-tree is unblanced, the entire tree is unblanced
                return -1 
            right_height = dfs_height(node.right)
            if right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1
        # -----------------------------------------
        return dfs_height(root) != -1        

        
        
from Tree import Tree

alist = [1,2,3,3,5,2,2]

tree1 = Tree()
for x in alist:
    tree1.add_sorted(x)  # unblanced 
print(tree1)    

tree2 = Tree()
for x in alist:
    tree2.add(x)  # balanced
print(tree2) 

sol = Solution()
r1 = sol.isBalanced(tree1.root)
r2 = sol.isBalanced(tree2.root)
print(r1, r2)

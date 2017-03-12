"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
"""

from Tree import Tree

# top solution 
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
        
t1 = Tree()
t2 = Tree()
'''
for i in range(10):
    t1.add(i)
    t2.add(i)
'''
t1.add(0)
t2.add(1)
sol = Solution()
r = sol.isSameTree(t1.root, t2.root)
print(r)    


# improvement 
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None or q is None:
            return p == q
        elif p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:  # p.val != q.val
            return False


# top solution: stack             
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack = [(p, q)]
        while stack:
            x, y = stack.pop()
            if x == None and y == None:
                continue
            elif x == None or y == None:
                return False
            elif x.val == y.val:
                stack.append((x.left, y.left))
                stack.append((x.right, y.right))
            else:  # x.val != v.val
                return False
        return True

        
# pythonic 
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x, left=None, right=None):
         self.val = x
         self.left = left
         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if  p and q and p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return p is q


s = Solution()
a = s.isSameTree(TreeNode(1,None,TreeNode(1)),TreeNode(1,None,TreeNode(1)))
print(a)
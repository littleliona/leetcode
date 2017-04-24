# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x, left=None, right=None):
         self.val = x
         self.left = left
         self.right = right

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        if root.left and not root.left.left and not root.left.right:  #是左叶子结点
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right) #其他情况


s = Solution()
a=s.sumOfLeftLeaves(TreeNode(3,TreeNode(9,TreeNode(5),TreeNode(6)),TreeNode(20,TreeNode(15),TreeNode(7))))
print(a)
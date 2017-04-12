#Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x, left=None, right=None):
         self.val = x
         self.left = left
         self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root


root = TreeNode('4',TreeNode('2',TreeNode('1'),TreeNode('3')),TreeNode('7',TreeNode('6'),TreeNode('9')))
s = Solution()
print(s.invertTree(root))
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return 

        stack = [root]
        res = []
        pre = None
        while stack:
            node = stack.pop()
            if pre:
                pre.left = None
                pre.right = node

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            pre = node

s = Solution()
root = TreeNode(1)
left = TreeNode(2)
left_ = TreeNode(3)
root.left = left
left.left = left_
a = s.flatten(root)
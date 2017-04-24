# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        tilt_left = self.sum_of_subtree(root.left)
        tilt_right = self.sum_of_subtree(root.right)
        return abs(tilt_right - tilt_left)+self.findTilt(root.left)+self.findTilt(root.right)

    def sum_of_subtree(self, root):
        if not root:
            return 0
        return root.val + self.sum_of_subtree(root.left) + self.sum_of_subtree(root.right)

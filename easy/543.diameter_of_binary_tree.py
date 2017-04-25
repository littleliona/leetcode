# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #leaf node depth = 1
        self.best = 0
    	def depth(root):
    		if not root:
        		return 0
        	left_depth = depth(root.left)
        	right_depth = depth(root.right)
        	self.best = max(self.best,left_depth+right_depth)
        	return 1 + max(left_depth,right_depth)
        
        depth(root)
        return self.best


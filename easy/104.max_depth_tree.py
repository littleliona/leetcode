# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x, left=None, right=None):
         self.val = x
         self.left = left
         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #mine
        if root == None:
        	return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        if left_depth > right_depth:
        	return left_depth+1
        if right_depth >= left_depth:
        	return right_depth+1 

        #easy
        return 1+max(map(self.maxDepth,(root.left,root.right))) if root else 0

root = TreeNode('A',TreeNode('B',TreeNode('C')))
s = Solution()
depth = s.maxDepth(root)
print(depth)
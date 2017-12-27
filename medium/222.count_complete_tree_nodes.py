# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left_depth = self.tree_depth(root.left)
        right_depth = self.tree_depth(root.right)

        if right_depth == left_depth:
            return pow(2, left_depth) + self.countNodes(root.right)
        else:
            return pow(2, right_depth) + self.countNodes(root.left)  

        
    def tree_depth(self, root):
        if not root:
            return 0

        return self.tree_depth(root.left) + 1
s = Solution()
a = s.longestValidParentheses(')()())')
print(a)

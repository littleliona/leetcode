# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # dfs + stack
        if not root:
            return 0

        res = 0
        stack = [(root,root.val)]
        while stack:
            node,value = stack.pop()
            if not node.left and not node.right:
               res += value
            if node.right:
                stack.append((node.right, value*10+node.right.val))
            if node.left:
                stack.append((node.left, value*10+node.left.val))
        
        return res
        #recursive
        self.res = 0
        self.dfs(root,0)
        return self.res 

    def dfs(self, root, value):
        if root:
            self.dfs(root.left, root.val + value * 10)
            self.dfs(root.right,root.val + value * 10)
            if not root.left and not root.right:
                self.res += value * 10 + root.val 


s = Solution()
a = s.checkInclusion("ab","eidbaooo")
print(a)

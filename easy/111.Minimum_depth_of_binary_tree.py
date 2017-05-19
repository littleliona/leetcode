
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        stack = []
        ans = []
        stack.append((root,1))

        while stack:
            x = stack.pop()
            node = x[0]
            if node.left:
                stack.append((node.left,x[1]+1))
            if node.right:
                stack.append((node.right,x[1]+1))

            if not node.left and not node.right:
                ans.append(x[1])

        return min(ans)

        
       
s = Solution()
a = s.minDepth()
print(a)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        #recursive
        res = []
        res = self.in_order(root)

        return res[k-1]

        #iterative
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
        

    def in_order(self, root):
        if not root:
            return []

        return self.in_order(root.left) + [root.val] + self.in_order(root.right)



s = Solution()
a = s.originalDigits("owoztneoer")
print(a)     

        


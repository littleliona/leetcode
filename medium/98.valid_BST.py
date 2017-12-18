# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import Counter
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #stack
        stack = []
        last_val = -float('inf')

        while stack or root:
            while(root):
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if root.val <= last_val:
                    return False
                last_val = root.val 
                root = root.right 

        return True

        #recursive
        if not root:
            return True

        L = self.pre_order(root)
        dic_ = Counter(L)
        return L == sorted(L) and max(dic.values()) == 1

    def pre_order(self, root):
        if not root:
            return []
        
        return self.pre_order(root.left) + [root.val] + self.pre_order(root.right)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        #method O(1)
        self.order = []
        self.prev = None
        self.inorder(root)
        if len(self.order) == 2:
            self.swap(self.order[0][0], self.order[1][1])
        elif len(self.order) == 1:
            self.swap(self.order[0][0], self.order[0][1])
        return

        #method O(n)
        L = []
        L = self.in_order(root)
        first, second = None, None 
        for i in range(1,len(L)):
            if not first and L[i-1].val > L[i].val:
                first = L[i-1]
                second = L[i]
            if first and L[i-1].val > L[i].val:
                second = L[i]

            first.val, second.val = second.val, first.val

    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        if self.prev and self.prev.val > root.val:
            self.order.append((self.prev, root))
        self.prev = root
        self.inorder(root.right)
        return
    
    def swap(self, r1, r2):
        r1.val, r2.val = r2.val, r1.val
        return

    def in_order(self,root):
        if not root:
            return []

        return self.in_order(root.left) + [root] + self.in_order(root.right)
s = Solution()
a = s.longestValidParentheses(')()())')
print(a)

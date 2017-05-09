# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x, left=None, right = None):
         self.val = x
         self.left = left
         self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #mine
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if root.right and root.left and root.left.val == root.right.val:
            return self.dfs(root.left) == self.dfs2(root.right)
            
        return False

        #recursively
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)

        #iteratively
        if root is None:
          return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
        return True

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        if left.val == right.val:
            outPair = self.isMirror(left.left, right.right)
            inPiar = self.isMirror(left.right, right.left)
            return outPair and inPiar
        else:
            return False

    def dfs(self, root):
        if not root:
            return []
        

        return self.dfs(root.left) + [root.val] + self.dfs(root.right)

    def dfs2(self, root):
        if not root:
            return []
        
        return self.dfs2(root.right) + [root.val] + self.dfs2(root.left)


s = Solution()
a = s.isSymmetric(TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(2,TreeNode(4),TreeNode(3))))
print(a)
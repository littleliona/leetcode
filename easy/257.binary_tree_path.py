# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x, left=None, right=None):
         self.val = x
         self.left = left
         self.right = right

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # dfs + stack
        if not root:
            return []
        
        res, stack = [], [(root, "")]
        while stack:
            node, ls = stack.pop()      #node为结点 ls是该结点前保存的路径
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.right:
                stack.append((node.right, ls+str(node.val)+"->"))
            if node.left:
                stack.append((node.left, ls+str(node.val)+"->"))
        return res


s = Solution()
a = s.binaryTreePaths(TreeNode(3,TreeNode(1,None,TreeNode(2))))
print(a)
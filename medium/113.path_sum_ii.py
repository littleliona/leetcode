# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfs(root, sum,[])

        return self.res

    def dfs(self, root, target, path):
        if not root:
            return 
        
        if not root.left and not root.right:
            if root.val == target:
                path += [root.val]
                self.res.append(path)
                return

        if root.left:
            self.dfs(root.left, target-root.val, path+[root.val])
            
        if root.right:
            self.dfs(root.right, target-root.val, path+[root.val])

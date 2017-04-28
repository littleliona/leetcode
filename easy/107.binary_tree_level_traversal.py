# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        height = self.getHeight(root)
        list_ = [[] for i in range(height)]
        self.level_from_bottom(root, list_, height-1)
        return list_


    def getHeight(self, root):
        if not root:
            return 0
        height_l = self.getHeight(root.left)
        height_r = self.getHeight(root.right)
        return 1 + max(height_l,height_r)

    def level_from_bottom(self, root, list_, level):
        if not root:
            return 
        list_[level].append(root.val)
        self.level_from_bottom(root.left,list_,level-1)
        self.level_from_bottom(root.right,list_,level-1)


s = Solution()
a = s.levelOrderBottom(11)
print(a)
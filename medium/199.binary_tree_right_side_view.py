# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # method_mine
        if not root:
            return []
        stack = [(root,1)]
        res = []
        level_tree = 0
        while stack:
            node,level = stack.pop(0)
            if level != level_tree:
                res.append(node)
                level_tree = level
            if node.right:
                stack.append((node.right,level+1))
            if node.left:
                stack.append((node.left,level+1))

        return res

        # method__same
        def collect(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)
                collect(node.right, depth+1)
                collect(node.left, depth+1)
        view = []
        collect(root, 0)
        return view


s = Solution()
a = s.grayCode(3)
print(a)


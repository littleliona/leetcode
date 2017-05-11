# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x, left=None, right=None):
         self.val = x
         self.left = left
         self.right = right

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        #easy #为了区分[12] [2]
        def convert(p):
            return "#" + str(p.val) + convert(p.left) + convert(p.right) if p else "$"
        
        return convert(t) in convert(s)

        #mine 首先dfs遍历，找到所有与t root相等的点，然后递归比较左右结点
        stack = []
        res = []
        stack.append(s)
        node = None
        x = 0
        while stack:
            node = stack.pop()
            if node:
                if node.val == t.val:
                    res.append(node)
                stack.append(node.left)
                stack.append(node.right)

        for i in range(len(res)):
            print(res[i].val)
        if res:
            for i in range(len(res)):
                x = x or self.compare_val(res[i],t)
            return bool(x)
        else:
            return False


    def compare_val(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return True and self.compare_val(s.left,t.left) and self.compare_val(s.right,t.right)

        return False




s = Solution()
a = s.isSubtree(TreeNode(1,TreeNode(1)),TreeNode(1))
print(a)




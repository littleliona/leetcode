class TreeNode(object):
     def __init__(self, x, left=None, right=None):
         self.val = x
         self.left = left
         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # O(n)
        # 直接在求深度的时候判断是否平衡
        # 首先求左右子树深度，如果左右子树不平衡或者该结点处不平衡，直接返回－1，否则返回深度
        # 判断结果是否！＝－1
        def check(root):
            if root is None:
                return 0
            left  = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
            
        return check(root) != -1



        #recursive O(n^2)
        # 首先判断左右子树是否平衡，平衡的话判断当前结点是否平衡
        # 因为对每个结点都求了其左右子树的深度，所以复杂度为O(n^2)
        # 一个递归求深度，一个递归求平衡
        if not root:
            return True

        if not self.isBalanced(root.left):
            return False

        if not self.isBalanced(root.right):
            return False

        depth_left = self.depth(root.left)
        depth_right = self.depth(root.right)
        
        if abs(depth_right - depth_left) >1:
            return False

        return True

    def depth(self, root):
        if not root:
            return 0

        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)

        return max(left_depth,right_depth)+1
  

s = Solution()
a = s.isBalanced(TreeNode(3,TreeNode(1,None,TreeNode(2))))
print(a)
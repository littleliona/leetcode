class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.msum = float('-inf')
        self.get_sum(root)
        return self.msum 


    def get_sum(self, root):
        if not root:
            return 0

        ls, rs = self.get_sum(root.left), self.get_sum(root.right)
        max_single_path = max(root.val+max(rs,ls), root.val)
        self.msum = max(self.msum, max_single_path, rs+ls+root.val)

        return max_single_path
    

# Definition for a binary tree node.
from collections import Counter
#class TreeNode(object):
#	def __init__(self, x, left=None, right=None):
#         self.val = x
#         self.left = left
#         self.right = right

#easy--faster 
import collections 
class Solution(object):
    def findFrequentTreeSum(self, root):
        if root == None: return []
        def getSum(node):
            if node == None: return 0
            s = node.val + getSum(node.left) + getSum(node.right)
            c[s] += 1
            return s
        c = collections.Counter()
        getSum(root)
        frequent = max(c.values())
        return [s for s in c.keys() if c[s] == frequent]

#mine
class Solution(object):
    def __init__(self):
        self.L = []

    def findFrequentTreeSum(self, root):
        self.calculate_Tree_Sum(root)
        self.L.sort()
        
        if len(self.L) == len(set(self.L)):
            return self.L
        else:
            dic = Counter(self.L)
            m = max(dic.values())
            return [key for key,value in dic.items() if value == m]


    def calculate_Tree_Sum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return 0
        
        root.val += self.calculate_Tree_Sum(root.left) + self.calculate_Tree_Sum(root.right)
        self.L.append(root.val)
        return root.val


        
s = Solution()
a = s.findFrequentTreeSum(TreeNode(5,TreeNode(2),TreeNode(-5)))
print(a)

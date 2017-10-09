class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key = lambda x:x[1])
        length = 0
        cur = float('-inf')
        for pair in pairs:
        	if cur < pair[0]:
        		cur, length = pair[1], length+1
        		


        return length



s = Solution()
a = s.findLongestChain([[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]])
print(a)
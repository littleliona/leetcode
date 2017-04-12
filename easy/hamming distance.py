class Solution(object):
    def hammingDistance(self, x, y):
    	dis = x ^ y
    	print(bin(dis).count('1'))

s = Solution()
s.hammingDistance(1,4)

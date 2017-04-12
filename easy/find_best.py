class Solution(object):
    def findComplement(self, num):
        i = 1
        while i <= num:
            i = i << 1
            print(i,'eee')
        print((i - 1) ^ num)

s = Solution()
s.findComplement(5)

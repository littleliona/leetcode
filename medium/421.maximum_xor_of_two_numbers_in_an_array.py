class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = mask = 0
        # a ^ b = c -> a = b ^ c
        for x in range(31, -1, -1):
            #mask不断加上1，从左到右
            mask += 1 << x
            #前缀集合
            prefixSet = set([n & mask for n in nums])
            #tmp是当前异或的最大值后面加一个1
            tmp = ans | 1 << x
            #如果tmp ^ set in set，说明tmp可以由set中的两个数异或得到
            for prefix in prefixSet:
                if tmp ^ prefix in prefixSet:
                    ans = tmp
                    break
        return ans


        
s = Solution()
a = s.findMaximumXOR([10, 2, 8])
print(a)     

        


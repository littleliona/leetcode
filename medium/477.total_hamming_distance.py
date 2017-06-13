class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #idea:计算出每一位上1的个数和0的个数，然后相乘

        #easy--fast
        return sum(b.count('0') * b.count('1') for b in zip(*map('{:032b}'.format, nums)))
        
        #easy-two
        ans = 0
        mask = 1
        for j in range(0, 32):
            ones = zeros = 0
            for num in nums:
                if num & mask:
                    ones += 1
                else:
                    zeros += 1
            ans += ones * zeros
            mask = mask << 1
        return ans

        #mine
        dic = {}
        dis = 0
        for num in nums:
            for i,x in enumerate(reversed(bin(num))):
                if x == '1':
                    if i not in dic:
                        dic[i] = 1
                    else:
                        dic[i] += 1


        for value in dic.values():
            dis += value * (len(nums) - value)

        return dis
        
s = Solution()
a = s.totalHammingDistance([4,14,2])
print(a)

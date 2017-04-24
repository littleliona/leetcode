class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        #mine
        dic = {}
        L = sorted(nums,reverse=True)
        L1 = []
        for n in range(len(L)):
            if n ==0:
                dic[L[n]] = "Gold Medal"
            elif n ==1:
                dic[L[n]] = "Silver Medal"
            elif n ==2:
                dic[L[n]] = "Bronze Medal"
            else:
                dic[L[n]] = str(n+1)

        for num in nums:
            L1.append(dic.get(num))

        return L1

        #easy
        sort = sorted(nums)[::-1]
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + map(str, range(4, len(nums) + 1))
        return map(dict(zip(sort, rank)).get, nums)



s = Solution()
print(s.findRelativeRanks([7,2,4,8,5,9]))
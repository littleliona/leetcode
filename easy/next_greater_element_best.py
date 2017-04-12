class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        dmap = {}
        stack = []
        for n in nums:
            while stack and stack[-1] < n:
                dmap[stack.pop()] = n
            stack.append(n)
        print [dmap.get(n, -1) for n in findNums]

s = Solution()
s.nextGreaterElement([2,0,1],[2,1,0,3])


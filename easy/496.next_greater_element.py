class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        #mine
        L = []
        flag = False;
        for n in findNums:
            i = nums.index(n)
            while(i != len(nums)-1):
                if nums[i+1]>n:
                    L.append(nums[i+1])
                    flag = True
                    break;
                else:
                    i = i+1
            if(flag == False):
                L.append(-1)
            flag = False
        return L

        #easy
        dmap = {}
        stack = []
        for n in nums:
            while stack and stack[-1] < n:
                dmap[stack.pop()] = n
            stack.append(n)
        print [dmap.get(n, -1) for n in findNums]

s = Solution()
s.nextGreaterElement([2,0,1],[2,1,0,3])


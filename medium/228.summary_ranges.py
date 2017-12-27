class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        #method_fast
        if not nums: return []
        res = []
        l = r = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == r+1:
                r += 1
            else:
                res.append(self.helper(l,r))
                l = r = nums[i]
                
        res.append(self.helper(l,r))
        return res
        
        #method_mine
        if not nums:
            return []

        stack = [nums[0]]
        res = []
        for num in nums[1:]:
            if num == stack[-1] + 1:
                stack.append(num)
            else:
                if len(stack) == 1:
                    res.append(str(stack.pop()))
                else:
                    res.append(str(stack[0])+'->'+str(stack[-1]))
                stack = []
                stack.append(num)
        if len(stack) == 1:
            res.append(str(stack.pop()))
        else:
            res.append(str(stack[0])+'->'+str(stack[-1]))

        return res 




    def helper(self,l,r):
        if l == r: return str(l)
        
        return str(l) + "->" + str(r)


        


s = Solution()
a = s.longestValidParentheses(')()())')
print(a)

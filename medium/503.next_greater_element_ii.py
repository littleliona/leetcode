class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #faster
        #Process it twice 
        #as it is a circular array to make sure that 
        #we can reread the next greater element after every element.
        #第一遍将最大值跟没找到最大值的index入栈  递减栈
        #第二遍相当于nums+nums
        stack, res = [], [-1] * len(nums)
        #only in Python 2
        for i in range(len(nums)) * 2:
            while stack and (nums[stack[-1]] < nums[i]):
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res

        #method_2
        stack, res = [], [-1] * len(nums)
        for i in range(len(nums)*2):
            while stack and (nums[stack[-1]] < nums[i%len(nums)]):
                res[stack.pop()] = nums[i%len(nums)]
            stack.append(i%len(nums))

        return res        

s = Solution()
a = s.nextGreaterElements([1,2,1])
print(a)
        


class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #dfs
        '''
        This is actually a DFS.  Use a visited map to keep track of visited node. If a 
number is visited before, then the set that starts at this number must be smaller then
 previous max. So we can safely skip this number. In total it's O(n) complexity.
        '''
        res = 0
        count = 0
        visited = [False]*len(nums)
        
        for i,num in enumerate(nums):
            count = 0
            while visited[i] == False:
                visited[i] = True
                count += 1
                i = nums[i]

            res = max(count,res)

        return res
            


s = Solution()
a = s.arrayNesting([5,4,0,3,1,6,2])
print(a)
        


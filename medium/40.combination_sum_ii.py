class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates = sorted(candidates)
        def dfs(remain, stack,index):
            if remain == 0 and stack not in result:
                result.append(stack)
                return 

            for i,item in enumerate(candidates[index:]):
                if item > remain: break
                else:
                    dfs(remain - item, stack + [item],i+index+1)
    
        dfs(target, [], 0)
        return result
        



s = Solution()
a = s.combinationSum2([10,1,2,7,6,1,5],8)
print(a)

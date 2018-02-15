class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        self.memo = set()   #memory dead ends
        target = stones[-1]
        stones = set(stones)

        return self.dfs(stones, 1, 1, target)

    def dfs(self, stones, cur_pos, step, target):

        if (cur_pos, step) in self.memo:
            return False
        
        if cur_pos == target:
            return True

        if cur_pos not in stones or cur_pos < 0 or cur_pos > target or step <= 0:
            return False

        candidate = [step-1,step,step+1]
        for c in candidate:
            if cur_pos + c in stones:
                if self.dfs(stones, cur_pos+c, c, target):
                    return True

        self.memo.add((cur_pos,step))
        return False

if __name__ == '__main__':
    s = Solution()
    a = s.canMeasureWater(2,6,5)
    print(a)

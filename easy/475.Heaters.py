import bisect
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        
        #method_1
        #[float('inf')]针对heaters长度为1的情况，防止越界
        
        heaters = sorted(heaters) + [float('inf')]  
        i = r = 0
        for x in sorted(houses):
            #找到距离当前house最近的heater
            while abs(heaters[i+1]-x) <= abs(heaters[i]-x):
                i += 1
            r = max(r, abs(heaters[i] - x))
        return r
        
        #binary_search
        heaters.sort()
        ans = 0
        
        for h in houses:
            #利用二分查找，找到不大于house的最大加热器坐标left，以及不小于house的最小加热器坐标right
            hi = bisect.bisect_left(heaters, h)
            left = heaters[hi-1] if hi-1 >= 0 else float('-inf')
            right = heaters[hi] if hi < len(heaters) else float('inf')
            ans = max(ans, min(h-left, right-h))

        return ans


        
        

        
s = Solution()
a = s.findRadius([1,2,3,4,5],[2,4])
print(a)
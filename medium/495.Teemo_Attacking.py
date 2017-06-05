class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        poison_time = 0
        for index in range(len(timeSeries)-1):
            if timeSeries[index+1] - timeSeries[index] < duration:
                poison_time += timeSeries[index+1] - timeSeries[index]
            else:
                poison_time += duration

        poison_time += duration
        return poison_time



        
s = Solution()
a = s.findPoisonedDuration([1,4],2)
print(a)

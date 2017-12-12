class Solution(object):
    def findMinDifference(self, A):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def convert(time):
            return int(time[:2]) * 60 + int(time[3:])

        # convert str to minutes(int)
        minutes = map(convert, A)
        # sort 
        minutes.sort()
        
        # 对第一个time add 60*24， append, circular array 
        minutes.append(60*24 + minutes[0])

        # 两两比较，找最小值
        return min(b - a for a, b in zip(minutes, minutes[1:]))




                
s = Solution()
a = s.findLength([1,2,3,2,1],[3,2,1,4,7])
print(a)

import collections 
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        #use dic to store the sum(exclude the last one)
        #find the max value 
        height = len(wall)
        dic = collections.defaultdict(int)
        for row in wall:
            sum_ = 0
            for column in row[:-1]:
                sum_ += column
                dic[sum_] += 1

    
        brick = max(value for key,value in dic.items()) if dic else 0
        return height - brick

  

s = Solution()
a = s.leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]])
print(a)     

        


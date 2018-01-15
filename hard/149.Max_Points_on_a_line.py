# Definition for a point.
class Point(object):
     def __init__(self, a, b):
         self.x = a
         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) <= 2:
            return len(points)
        max_pts = 0
        for i in range(len(points)-1):
            pi = points[i]
            equal = 0
            verticle = 0
            cur = 0
            slopes = {}
            for j in range(i+1, len(points)):
                pj = points[j]
                if pi.x == pj.x and pi.y == pj.y:
                    equal += 1
                elif pi.x == pj.x:
                    verticle += 1
                else:
                    slope =  (pj.y - pi.y) * 100.0 /(pj.x - pi.x)
                    if slope in slopes:
                        slopes[slope] += 1
                    else:
                        slopes[slope] = 1
                    cur = max(cur, slopes[slope])
            max_pts = max(max_pts, max(cur, verticle) + equal + 1) 
        return max_pts

s = Solution()
a = s.maxPoints([Point(1,3),Point(1,1),Point(2,2),Point(0,2)])
print(a)

        

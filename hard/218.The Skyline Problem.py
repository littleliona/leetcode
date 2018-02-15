import heapq
class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """

        def add_sky(pos, height):
            # 高度发生变化的时候添加到sky
            if sky[-1][1] != height:
                sky.append((pos,height))

        
        sky = [(-1,0)]

        live = []
        position = sorted([b[1] for b in buildings] + [b[0] for b in buildings])
        
        i = 0
        for t in position:
            # add new buildings when left side is lefter than position t
            while i < len(buildings) and buildings[i][0] <= t:
                heapq.heappush(live, (-buildings[i][2], buildings[i][1]))
                i += 1
            
            # remove the past buildings whose right side is lefter than position t -- update the height
            while live and live[0][1] <= t:
                heapq.heappop(live)
            
            # pick the highest existing building at this moment
            h = -live[0][0] if live else 0

            add_sky(t,h)

        return sky[1:]

if __name__ == '__main__':
    s = Solution()
    a = s.wordBreak("leetcode",["leet", "code"])
    print(a)

from collections import defaultdict
class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """

        #生成一个字典
        #pid:childid
        d = defaultdict(list)
        for i,PPID in enumerate(ppid): 
            d[PPID].append(pid[i])

        bfs = [kill]
        for i in bfs: bfs.extend(d.get(i, []))
        return bfs


s = Solution()
a = s.killProcess([6,1,3,9,5,8,7,4,10],[5,8,4,5,10,5,3,8,0],10)
print(a)
        


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #method_dfs
        graph = [[] for _ in xrange(numCourses)]
        visit = [0 for _ in xrange(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        def dfs(i):
            # if ith node is marked as being visited, then a cycle is found
            if visit[i] == -1:
                return False
            # if it is done visted, then do not visit again
            if visit[i] == 1:
                return True
            # mark as being visited
            visit[i] = -1
            # visit all the neighbours

            for j in graph[i]:
                if not dfs(j):
                    return False
            # after visit all the neighbours, mark it as done visited
            visit[i] = 1
            return True
        for i in xrange(numCourses):
            if not dfs(i):
                return False
        return True 

        #method___
        if numCourses<2 or len(prerequisites)<2:
            return True
        #prerequisites.sort()
        while True:
            count=0
            mark = [True]*numCourses
            for pre in prerequisites:
                mark[pre[0]] = False
            for pre in prerequisites:
                if mark[pre[1]]:
                    count+=1
                    prerequisites.remove(pre)
            if prerequisites==[]:
                return True
            elif count==0:
                return False



s = Solution()
a = s.partition('aab')
print(a)

from collections import defaultdict
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        if n == 1: return [0]
        neighbors = collections.defaultdict(list)
        degrees = collections.defaultdict(int)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
            degrees[u] += 1
            degrees[v] += 1

        # First find the leaves
        preLevel, unvisited = [], set(range(n))
        for i in range(n):
            if degrees[i] == 1: preLevel.append(i)

        while len(unvisited) > 2:
            thisLevel = []
            for u in preLevel:
                unvisited.remove(u)
                for v in neighbors[u]:
                    if v in unvisited: 
                        degrees[v] -= 1
                        if degrees[v] == 1: thisLevel += [v]
            preLevel = thisLevel

        return preLevel
        

if __name__ == '__main__':
    s = Solution()
    a = s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
    print(a)

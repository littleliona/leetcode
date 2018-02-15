from collections import defaultdict 

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        dic = defaultdict(list)
        for ticket in tickets:
            dic[ticket[0]].append(ticket[1])
        
        self.route = ["JFK"]
        
        def dfs(start):
            if len(self.route) == len(tickets)+1:
                return True
            
            myDsts = sorted(dic[start])
            for dst in myDsts:
                dic[start].remove(dst)
                self.route += dst,
                if dfs(dst):
                    return True
                self.route.pop()
                dic[start] += dst,
            return False

        dfs("JFK")
        return self.route

   
if __name__ == '__main__':
    s = Solution()
    a = s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
    print(a)

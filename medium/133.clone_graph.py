# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        
        if not node:
            return node

        stack = [node]
        root = UndirectedGraphNode(node.label)
        visit[node.label] = root 

        while stack:
            top = stack.pop()

            for n in top.neighbors:
                if n.label not in visit:
                    stack.append(n)
                    visit[n.label] = UndirectedGraphNode(n.label)

                visit[top.label].neighbors.append(visit[n.label])


s = Solution()
a = s.partition('aab')
print(a)

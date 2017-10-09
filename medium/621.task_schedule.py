from collections import Counter
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_counts = Counter(tasks).values()
        M = max(task_counts)
        M_num = task_counts.count(M)

        return max(len(tasks), (M-1) * (n+1) + M_num)
    

s = Solution()
a = s.leastInterval(['A','A','A','A','A','B','B','B','B','C','C','C','D','D'], 2)
print(a)
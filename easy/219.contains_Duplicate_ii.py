from collections import Counter 
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        #mine
        if len(nums) == len(set(nums)):
            return False

        num = 0
        dic = Counter(nums)
        for key,v in dic.items():
            if v > 1:
                num = key
                break

        L = [i for i,v in enumerate(nums) if v == num]
        return min(L[i+1]-L[i] for i in range(len(L)-1)) <= k


        #easy
        if len(nums) == len(set(nums)):
            return False
    

        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False


s = Solution()
a = s.containsNearbyDuplicate([1,0,1,1],2)
print(a)
    


        






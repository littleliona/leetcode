class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        #mine
        a = 0
        b = len(numbers)-1

        while(True):
            if numbers[a] + numbers[b] < target:
                a+=1
            elif numbers[a] + numbers[b] > target:
                b-=1
            elif numbers[a] + numbers[b] == target:
                return [a+1,b+1]

        #binary search
        for i in range(len(numbers)):
            l, r = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1
        #dict
        dic = {}
        for i,num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1,i+1]
            dic[num] = i


s = Solution()
print(s.twoSum([2, 7, 11, 15],9))
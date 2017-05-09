from functools import reduce 
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #mine_1
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        
        pre = 1
        for i in range(len(digits)-1,-1,-1):
            if pre == 1:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] +=1
                    pre = 0
                    return digits

        if pre == 1:
            digits.insert(0,1)
            return digits
        
        #mine_2 key: int type is not iterative so turn it into str type
        num = reduce(lambda x,y:x*10+y,digits)
        return [int(i) for i in str(num+1)]




s = Solution()
a = s.plusOne([8,9,9,9])
print(a)
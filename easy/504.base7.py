class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        #mine
        s = ""
        a = num
        num = abs(num)

        while(num>=7):
            s += str(num%7)
            num = int(num/7)
        s+=str(num)
        return "-"+s[::-1] if a<0 else s[::-1]

        #recursive
        if num < 0: return '-' + self.convertToBase7(-num)
        if num < 7: return str(num)
        return self.convertToBase7(num // 7) + str(num % 7)




s = Solution()
a = s.convertToBase7(-7)
print(a)
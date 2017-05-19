class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(n-1):
            temp = ''
            count = 0
            let = s[0]

            for char in s:
                if char == let:
                    count+=1
                else:
                    temp += str(count) + let
                    count = 1
                    let = char
            temp += str(count) + let
            s = temp

        return s
        

        
       
s = Solution()
a = s.countAndSay(4)
print(a)
class Solution:
    def singleNumber(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        #用one记录到当前计算的变量为止，二进制1出现“1次”（mod 3 之后的 1）的数位。
        #用two记录到当前计算的变量为止，二进制1出现“2次”（mod 3 之后的 2）的数位。
        #当one和two中的某一位同时为1时表示二进制1出现3次，此时需要清零。即用二进制模拟三进制计算。最终one记录的是最终结果。
        one = 0; two = 0; three = 0
        for i in range(len(A)):
            two |= A[i] & one      #two为1时，不管A[i]为什么，two都为1        
            one = A[i] ^ one       #异或操作，都是1就进位        
            three = ~(one & two)   #以下三步的意思是：如果one和two都为1时，就清0，反之则保持原来状态。
            one &= three
            two &= three
        return one


s = Solution()
a = s.singleNumber([1,1,1,2,2,2,3])
print(a)



class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        dict_ = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        str_ = ""

        if num<0:
            num = 2**32 - abs(num)

        while num>=16:
            str_+=dict_.get(num%16)
            num = num //16
        str_+=dict_.get(num)
        return str_[::-1]
     
        	
        	

s = Solution()
a = s.toHex(-100000)
print(a)
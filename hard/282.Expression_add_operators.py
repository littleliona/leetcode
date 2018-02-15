class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        results = []
        self.helper(0, num, 0, 0, "", target, results)
        return results
    
    
    def helper(self, start, num, cur_val, prev, path, target, res):
        if start == len(num):
            if cur_val == target:
                res.append(path)
        else:
            for i in range(start, len(num)):
                number_s = num[start:i+1]
                number = int(number_s)
                if number_s[0] == "0" and len(number_s) > 1: ### IGNORE INPUT LIKE "00", "005", "0006"
                    continue
                if start == 0:
                    self.helper(i+1, num, number, number, number_s, target, res)
                else:
                    self.helper(i+1, num, cur_val+number, number, path+"+"+number_s, target, res)
                    self.helper(i+1, num, cur_val-number, number*-1, path+"-"+number_s, target, res)
                    self.helper(i+1, num, cur_val-prev+number*prev, number*prev, path+"*"+number_s, target, res)
            return


if __name__ == '__main__':
    s = Solution()

    a = s.addOperators("105",5)
    print(a)
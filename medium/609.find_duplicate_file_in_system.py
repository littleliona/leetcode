import re
from collections import defaultdict
class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        #先拆出来root_path
        #再拆出来file_name and file_content
        #放入字典中，输出
        res = []
        dic = defaultdict(list)
        for path in paths:
            file_split = path.split(' ')
            file_root = file_split[0]
            for file in file_split[1:]:
                file_=file_.split("(")              #faster
                #file_ = re.split('[(]+',file)      #slower 
                file_content = file_[1]
                file_name = file_[0]
                dic[file_content].append(file_root+'/'+file_name)

        for key,value in dic.items():
            if len(value) > 1:
                res.append(value)

        return res


     
s = Solution()
a = s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])
print(a)
        


class Solution(object):
    def findTheDifference(self, s, t):
        for i in t:
            if s.count(i) != t.count(i):
                return i
        """
        :type s: str
        :type t: str
        :rtype: str
        """
       
        # res = ""
        
        # for i in s:
        #     if i not in t:
        #         res += i  

        # for j in t:
        #     if j not in s:
        #         res += j

        # return res                      
             
        
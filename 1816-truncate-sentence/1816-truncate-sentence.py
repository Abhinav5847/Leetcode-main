class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        li = s.split()
        
        res = ""
        for i in range(k):
            res += li[i] + " "
        return res.strip()    

        
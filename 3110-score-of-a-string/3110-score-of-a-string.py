class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = []
        for i in s:
            res.append(ord(i))

        s = 0
        for i in range(len(res)-1):
            s += abs(res[i] - res[i+1])    

        return s    
        
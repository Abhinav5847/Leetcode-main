class Solution(object):
    def maxDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        res = set(s)
        final = list(res)

        return len(final)
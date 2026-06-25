class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        vw = "aeiou"

        vw_count = 0

        cn_count = 0

        for i in s:

            if i in vw:

                if s.count(i) > vw_count:

                    vw_count = s.count(i)

            elif s.count(i) > cn_count:
                cn_count = s.count(i)

        return cn_count + vw_count             



        
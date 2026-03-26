class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        # wd = s.strip()
        # if len(wd) >= 1:
        #    res = wd.split(" ")
        #    final = [i for i in res if i.isalpha() or len(i) > 1]
        #    print(final)
        #    return len(final)
        # else:
        #     return 0

        res = s.split()
        
        return len(res)

        
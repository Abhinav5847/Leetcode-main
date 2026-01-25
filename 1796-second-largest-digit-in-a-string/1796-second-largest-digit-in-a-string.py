class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = []
        
        for i in s:
            if i.isdigit():
                res.append(int(i))

        fin = set(res)

        out = list(fin)

        out.sort(reverse = True)

        if len(out) <= 1:
            return -1
        else:
           return out[1]                        
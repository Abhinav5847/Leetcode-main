class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        l = list(s)

        # for i in s:
        #     if i == i.upper():
        #         up.append(i)
        #     else:
        #         lw.append(i)

        l.sort(reverse=True)
        # print(up)
        d =""
        for i in l:
            if i.lower() in l and i.upper() in l:
                return i.upper()    
            else:
                pass
        return d                          
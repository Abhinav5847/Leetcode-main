class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        item = word.lower()
        res = []
        for i in item:
            if i in res:
                pass
            else:
                res.append(i)
        c = 0
        for i in res:
            if i in word and i.upper() in word:
                c += 1 
                print(i)

        return c                  


    
        
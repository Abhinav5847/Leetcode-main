class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        splt = text.split()
        splt.sort(key=len)
        res =  " ".join(splt)
        final = res.lower()
        return final.capitalize()
        
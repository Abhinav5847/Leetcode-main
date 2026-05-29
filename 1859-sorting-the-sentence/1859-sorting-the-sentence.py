class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        li = s.split(" ")
        li.sort(key=lambda i:i[-1])

        return " ".join([i[:-1] for i in li])

        
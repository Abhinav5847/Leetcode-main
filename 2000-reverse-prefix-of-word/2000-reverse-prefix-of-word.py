class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        ind = 0
        for i in word:
            if i == ch:
                ind = word.index(i)

        part = word[:ind+1]

        final = part[::-1] + word[ind+1:]

        return final        

        
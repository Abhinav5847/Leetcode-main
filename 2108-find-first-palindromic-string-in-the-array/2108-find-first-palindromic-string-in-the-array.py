class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        final = []
        for i in words:
            rev = i[::-1]
            if i == rev:
                return i

        return ""       

         
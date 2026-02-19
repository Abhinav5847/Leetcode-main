class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        res = list(s.lower())

        fin = [i for i in res if i != " " and i.isalpha() or i.isdigit()]

        wd = "".join(fin)

        rv = wd[::-1]

        if wd == rv:
            return True
        else:
            return False    
        
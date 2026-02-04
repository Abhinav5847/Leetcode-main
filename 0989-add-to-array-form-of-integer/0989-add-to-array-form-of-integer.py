class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = ""
        for i in num:
            res += str(i)

        n = int(res) + k

        res = str(n)
        
        li = []
        for i in res:
            li.append(int(i))

        return li    

        
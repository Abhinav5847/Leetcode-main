class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
    
        res = []
        for i in arr:
            if i == arr.count(i):
                res.append(i)

        if len(res) > 0:
            return max(res)
        else:
            return -1                

        
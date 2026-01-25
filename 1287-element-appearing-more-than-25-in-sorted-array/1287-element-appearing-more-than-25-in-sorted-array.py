class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        mid = len(arr) // 2
        le = mid // 2

        for i in arr:
            if arr.count(i) > le:
                return i
                
        
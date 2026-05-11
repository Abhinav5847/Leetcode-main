class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        res = [str(i) for i in nums]
        single = []
        double = []
        for i in res:
            if len(i) == 1:
                single.append(int(i))
            else:
                double.append(int(i))    

        if sum(single) > sum(double) or sum(double) > sum(single):
            return True
        else:
            return False

        
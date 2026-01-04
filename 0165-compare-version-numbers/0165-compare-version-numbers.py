class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        n1 = version1.split(".")
        n2 = version2.split(".")

        length = max(len(n1), len(n2)) 
        for i in range(length):
            num1 = int(n1[i]) if i < len(n1) else 0
            num2 = int(n2[i]) if i < len(n2) else 0

            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1 

        return 0                         
        
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        rich = sum(accounts[0])

        for i in accounts:
            if sum(i) > rich:
                rich = sum(i)

        return rich        

   

        
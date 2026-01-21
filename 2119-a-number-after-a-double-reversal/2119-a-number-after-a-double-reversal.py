class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        first = str(num)[::-1]
        scnd = str(int(first))[::-1]

        if int(scnd) == num:
            return True
        else:
            return False    


        # nums = str(num)

        # if len(nums) == 1:
        #     return True

        # res = ""    
        # for i in nums:
        #     if int(i) != 0:
        #         res += i

        # firstrev = res[::-1]
        # scndrev = firstrev[::-1]

        # if int(scndrev) == num:
        #     return True
        # else:
        #     return False                          

        
        
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        sum_nums = sum(nums[:k])

        max_sum = sum_nums

        for i in range(k,len(nums)):

            sum_nums = sum_nums - nums[i-k] + nums[i]

            max_sum = max(max_sum,sum_nums)

        print(max_sum)

        return max_sum / float(k)    



        

        
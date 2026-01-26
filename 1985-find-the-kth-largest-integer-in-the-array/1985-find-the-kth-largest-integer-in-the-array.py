class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        li = []

        for i in nums:
            li.append(int(i))

        li.sort(reverse = True)

        res = li[k-1]

        return str(res)
        
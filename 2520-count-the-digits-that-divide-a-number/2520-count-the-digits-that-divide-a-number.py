class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        item = str(num)

        li = [] 
        for i in item:
            li.append(int(i))

        count = 0

        for i in li:
            if num % i == 0:
                count += 1

        return count        
class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        # res = []
        # for i in words:
        #     if x in i:
        #         ind = words.index(i)
        #         res.append(ind)
        # return res  
        res = []
        for i in range(0,len(words)):
            if x in words[i]:
                res.append(i)
        return res              



        
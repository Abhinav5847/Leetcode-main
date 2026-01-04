class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # if len(word) < 3:
        #     return False
        # vw = set("aeiouAEIOU")
        # hasvw = False
        # hasc = False 

        # for i in word:
        #     if not i.isalnum():
        #         return False
        #     if i.isalpha():
        #         if i in vw:
        #             hasvw = True
        #         else:
        #             hasc = True 

        # return hasvw and hasc 
        if len(word) < 3:
            return False 

        vw = set("aeiouAEIOU")
        hasvw = False
        hascn = False

        for i in word:
            if not i.isalnum():
                return False
            if i.isalpha():
                if i in vw:
                    hasvw = True
                else:
                    hascn = True 

        return hasvw and hascn                                           

        
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aeiou'
        wd = s.split(' ')
        res = []

        el_one = wd[0]
        res.append(el_one)

        first_count = 0
        for i in el_one:
            if i in vowels:
                first_count += 1

        
        for i in wd[1:]:
            scnd_count=0
            for j in i:
                if j in vowels:
                    scnd_count += 1

            if first_count == scnd_count:
                res.append(i[::-1])
            else:
                res.append(i)

        final = " ".join(res)
        return final            

                
        
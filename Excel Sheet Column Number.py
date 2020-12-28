import string
class Solution:
    def titleToNumber(self, s: str) -> int:
        length = len(s)
        letters = string.ascii_uppercase
        if length == 1 :
            return letters.index(s) +1
        else :
            total = 0
            for i in range(length-1):
                n = letters.index(s[i]) + 1
                total += ((26**(length-i-1))*n)
            total += letters.index(s[-1]) +1
            return total

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        minLength = min(len(st) for st in strs )
        longestCommonPrefix = strs[0]
        i = 0
        j = 0
        while(j < minLength):
            for st in strs:
                if (st[i] != longestCommonPrefix[i]):
                    j=minLength
                    break
            if(j != minLength):
                i += 1
                j += 1
        if i == 0:
            return ''
        else:
            return longestCommonPrefix[:i]
        

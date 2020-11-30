#https://leetcode.com/problems/defuse-the-bomb/submissions/


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        length = len(code)
        if k ==0:
            return [0]*length
        a=code+code
        
        if k>0:
            for i in range(length):
                code[i]=sum(a[i+1:i+1+k])

        if k<0:
            for i in range(length):
                code[i]=sum(a[length+i+k:length+i]) 
        return code

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        l =''
        for i in range(1, n+ 1):
            l += bin(i).replace("0b","")
            
        return int(l,2) %(10**9 + 7)
        

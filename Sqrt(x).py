class Solution:
    def mySqrt(self, x: int) -> int:
        a = x
        b = 1
        n = .001
        while a-b>n :
            a = (a+b)/2
            b= x/a
            
        return int(round(a))
        

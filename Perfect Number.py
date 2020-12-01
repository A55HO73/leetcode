from math import sqrt
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum_ = 0 - num
        for i in range( 1, int(sqrt(num))+ 1 ):
            if num % i == 0:
                sum_ += i 
                m = num // i
                if m != i :
                    sum_ += m
                    
        return sum_ == num

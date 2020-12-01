class Solution:
    def reverse(self, x: int) -> int:
        if x == 0 :
            return 0
        elif x > 0 :
            number =  int(str(x)[::-1])
            if number > 2**31-1:
                return 0
            else :
                return number
        elif x < 0:
            x *= (-1)
            number =-1 * int(str(x)[::-1])
            if number < -2**31 :
                return 0 
            else :
                return number

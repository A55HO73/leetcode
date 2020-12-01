class Solution:
    def countDigitOne(self, n: int) -> int:
        countr = 0
        for i in range( 1,  n+1 , 10):
            divider = i * 10
            countr += (n / divider) * i + min(max(n % divider - i + 1, 0), i)
        return int(countr)

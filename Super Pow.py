class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        return pow(a, int("".join(str(c) for c in b)) , mod=1337)
        

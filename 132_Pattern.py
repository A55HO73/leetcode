from math import inf
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] 
        ref = -inf
        for x in reversed(nums): 
            if (x < ref): 
                return True 
            while (stack and stack[-1] < x): 
                ref = stack.pop()
            stack.append(x)
        return False

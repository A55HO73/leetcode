class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        x = sorted(heights)
        count= 0
        for i in range(len(x)):
            if x[i] != heights[i]:
                count+= 1
            else :
                continue
                
        return count
        

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        length = len(arr)
        f = False
        for i in range(length - 2):
            if arr[i] % 2 ==1 :
                if arr[i+1] %2 == 1 and arr[i+2] %2== 1 :
                    f = True
                    break

                    
        return f

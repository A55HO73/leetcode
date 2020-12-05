from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        numf= Counter(nums)
        nums.sort(reverse=True) 
        nums.sort(key=numf.__getitem__)
        return nums

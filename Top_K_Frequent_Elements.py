from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dl = dict(Counter(nums))
        dsl = sorted(dl,key=dl.get,reverse= True)
        return dsl[:k]

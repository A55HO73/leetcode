#use python 3.9 


class Solution:
    def minDays(self, n: int) -> int:
        q = [(0,n)]
        nums = set()
        while q:
            x, curr = heapq.heappop(q)
            if curr==1: 
                return x+1
            if curr not in nums:
                nums.add(curr)
                heapq.heappush(q,(x+curr%2+1, curr//2))
                heapq.heappush(q,(x+curr%3+1, curr//3))
        return n

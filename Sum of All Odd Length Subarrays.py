class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        kq = 0
        for i in range(len(arr)):
            count, Sum = 0, 0
            for j in range(i,len(arr)):
                Sum  += arr[j]
                count +=1
                if count %2==1:
                    kq += Sum
        return kq

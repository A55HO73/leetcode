class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        i = 0
        lenght = len(A)
        while (i + 1 < lenght and A[i] < A[i+1]):
            i += 1
        if (i == 0 or i == lenght -1 ):
            return False 
        while (i + 1 < lenght and A[i] >A[i+1])):
            i += 1
        return i == lenght -1

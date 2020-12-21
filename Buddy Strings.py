class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        lena = len(A)
        lenb = len(B)
        if lena != lenb: 
            return False
        
        if A == B:
            if lena - len(set(A)) >= 1 :
                return True
            else:
                return False
        diff = []
        for i in range(lena):
            if A[i] != B[i]:
                diff.append(i)
                if len(diff) > 2: 
                    return False
                
        if len(diff) != 2: 
            return False
        if A[diff[0]] == B[diff[1]] and A[diff[1]] == B[diff[0]]:
            return True
        
        return False

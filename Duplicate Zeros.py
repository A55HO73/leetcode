class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        lenght = len(arr)
        zeros =[]
        for i in range(lenght):
            if arr[i] == 0 :
                zeros.append(i)
                
                
        for i in range(len(zeros)):
            arr.insert(zeros[i] +1 +i,0)
            arr.pop()

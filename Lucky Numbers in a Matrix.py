class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        luckyNumber=[]
        lenght = len(matrix)
        for i in range(0,lenght):
            min_ = min(matrix[i])              
            inx = matrix[i].index(min_)
            flag = True
            for j in range (0,lenght):      
                if matrix[j][inx] > matrix[i][inx]:
                    f = False
            if flag:
                luckyNumber.append(min_)
        return luckyNumber

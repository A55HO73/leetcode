class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = 0
        flag =False
        for i in nums:
            if i==1:
                if count<k and flag ==True:
                    return False
                flag = True
                count = 0
            if flag == True and i==0:
                count+=1
        return True

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l =[]
        lenght = len(nums)

        if lenght == 0 :
            return l
        else :
            temp_start = nums[0]
            temp_end = nums[0]

            for i in range(1, lenght):
                if nums[i] == nums[i-1] + 1:
                    temp_end = nums[i]
                else :
                    if temp_end ==temp_start :
                        l.append(str(temp_start))
                    else :
                        l.append(str(temp_start) +"->" + str(temp_end))
                    temp_end = nums[i]
                    temp_start = nums[i]

            if temp_end ==temp_start :
                l.append(str(temp_start))
            else :
                l.append(str(temp_start) +"->" + str(temp_end))
            return l 

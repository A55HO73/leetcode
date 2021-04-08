class Solution:
    

    def maxSubArray(self, nums: List[int]) -> int:
    

        maximum = nums[0]
        temp = nums[0]
        for i  in range(1, len(nums)):
            temp = max(temp + nums[i], nums[i])
            maximum = max( maximum,temp)
            
        return maximum
            

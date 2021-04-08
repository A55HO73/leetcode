int comp (int a, int b)
{
    return a>= b ? a:b;
}

int maxSubArray(int* nums, int numsSize){
    int max = nums[0], temp = nums[0];
    for( int i =1; i < numsSize; i++)
    {
        temp = comp(temp + nums[i], nums[i]);
        max = comp(max, temp);
    }
    return max;
}

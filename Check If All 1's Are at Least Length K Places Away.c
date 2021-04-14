

bool kLengthApart(int* nums, int numsSize, int k){
    int i, count = 0;
    bool flag = false;
    for(i = 0 ; i < numsSize; i++)
    {
        if (nums[i] == 1)
        {
            if(count < k && flag)
            {
                return false;
            }
            flag = true;
            count = 0;
        }
        if(flag && nums[i] == 0 )
        {
            count += 1;
        }
    }
    return true;
}

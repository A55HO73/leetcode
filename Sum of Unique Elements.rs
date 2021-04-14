impl Solution {
    pub fn sum_of_unique(nums: Vec<i32>) -> i32 {
        let mut sum = 0;
        for x in nums.iter()
        {
            let mut count = 0;
            for y in nums.iter()
            {
                if (*x == *y )
                {
                    count += 1;
                }
            }
            if (count == 1)
            {
                sum += *x;
            }
        }
        return sum;
    }
}


impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        let mut i = 0;
        let LEN = nums.len();
        if (nums[LEN -1] < target)
        {
            return  nums.len() as i32;
        }
        while i < LEN
        {
            if ( nums[i] < target)
            {
                i += 1;
            }
            else {
                return i as i32;
            }
        }
        return 0;
    }
}

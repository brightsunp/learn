/**
* Given an integer array nums, find the subarray with the largest sum, and return its sum.
*/
using TestMain.Definitions;

namespace TestMain.DynamicProgramming
{
    class MaxSubArray : Solution
    {
        public override void Run()
        {
            AssertEqual(6, MaxSubArrayNative(new int[] { -2, 1, -3, 4, -1, 2, 1, -5, 4 }));
            AssertEqual(1, MaxSubArrayNative(new int[] { 1 }));
            AssertEqual(23, MaxSubArrayNative(new int[] { 5, 4, -1, 7, 8 }));

            AssertEqual(6, MaxSubArrayConstant(new int[] { -2, 1, -3, 4, -1, 2, 1, -5, 4 }));
            AssertEqual(1, MaxSubArrayConstant(new int[] { 1 }));
            AssertEqual(23, MaxSubArrayConstant(new int[] { 5, 4, -1, 7, 8 }));
        }

        // Define sub problem: dp[i] is the max sub array which must have nums[i] as ending.
        private int MaxSubArrayNative(int[] nums)
        {
            var dp = new int[nums.Length];
            dp[0] = nums[0];
            int res = dp[0];
            for (int i = 1; i < nums.Length; i++)
            {
                dp[i] = nums[i] + (dp[i - 1] > 0 ? dp[i - 1] : 0);
                if (dp[i] > res)
                {
                    res = dp[i];
                }
            }
            return res;
        }

        private int MaxSubArrayConstant(int[] nums)
        {
            int cur = nums[0], res = nums[0];
            for (int i = 1; i < nums.Length; i++)
            {
                // cur = Max(nums[i], nums[i] + cur)
                cur = nums[i] + (cur > 0 ? cur : 0);
                if (cur > res)
                {
                    res = cur;
                }
            }
            return res;
        }
    }
}

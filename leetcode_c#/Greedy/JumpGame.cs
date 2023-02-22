/**
* You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position. 
* 
* Return true if you can reach the last index, or false otherwise.
*/
using System;
using TestMain.Definitions;

namespace TestMain.Greedy
{
    class JumpGame : Solution
    {
        public override void Run()
        {
            AssertTrue(CanJumpDp(new int[] { 2, 3, 1, 1, 4 }));
            AssertTrue(!CanJumpDp(new int[] { 3, 2, 1, 0, 4 }));

            AssertTrue(CanJumpGreedy(new int[] { 2, 3, 1, 1, 4 }));
            AssertTrue(!CanJumpGreedy(new int[] { 3, 2, 1, 0, 4 }));
        }

        private bool CanJumpDp(int[] nums)
        {
            var dp = new bool[nums.Length];
            dp[0] = true;
            for (int i = 1; i < nums.Length; i++)
            {
                for (int j = i - 1; j >= 0; j--)
                {
                    if (dp[j] && nums[j] >= i - j)
                    {
                        dp[i] = true;
                        break;
                    }
                }
            }

            return dp[nums.Length - 1];
        }

        private bool CanJumpGreedy(int[] nums)
        {
            int farest = nums[0];
            for (int i = 1; i < nums.Length; i++)
            {
                if (i > farest)
                {
                    return false;
                }
                farest = Math.Max(farest, i + nums[i]);
            }
            return true;
        }
    }
}

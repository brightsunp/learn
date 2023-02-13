/**
* Given an integer array nums, return the length of the longest strictly increasing subsequence.
*/
using System.Collections.Generic;
using TestMain.Definitions;
using TestMain.Snippets;

namespace TestMain.DynamicProgramming
{
    class LongestIncreasingSubsequence : Solution
    {
        public override void Run()
        {
            AssertEqual(4, LengthOfLisDp(new int[] { 10, 9, 2, 5, 3, 7, 101, 18 }));
            AssertEqual(4, LengthOfLisDp(new int[] { 0, 1, 0, 3, 2, 3 }));
            AssertEqual(1, LengthOfLisDp(new int[] { 7, 7, 7, 7, 7, 7, 7 }));

            AssertEqual(4, LengthOfLisGreedy(new int[] { 10, 9, 2, 5, 3, 7, 101, 18 }));
            AssertEqual(4, LengthOfLisGreedy(new int[] { 0, 1, 0, 3, 2, 3 }));
            AssertEqual(6, LengthOfLisGreedy(new int[] { 3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12 }));
        }

        // Define sub problem: dp[i] is the length of LIS which must have nums[i] as ending.
        // O(n*n) time and O(n) space
        private int LengthOfLisDp(int[] nums)
        {
            var dp = new int[nums.Length];
            dp.Populate(1);
            int res = 1;
            for (int i = 1; i < nums.Length; i++)
            {
                for (int j = i - 1; j >= 0; j--)
                {
                    if (nums[i] > nums[j] && dp[j] + 1 > dp[i])
                    {
                        dp[i] = dp[j] + 1;
                    }
                }
                if (dp[i] > res)
                {
                    res = dp[i];
                }
            }
            return res;
        }

        // Greedy with Binary Search: keep one subsequence which always has the longest length.
        // O(n*log n) time and O(n) space
        private int LengthOfLisGreedy(int[] nums)
        {
            var sub = new List<int> { nums[0] };
            for (int i = 1; i < nums.Length; i++)
            {
                if (nums[i] > sub[sub.Count - 1])
                {
                    sub.Add(nums[i]);
                }
                else
                {
                    sub[SearchInsert(sub, nums[i])] = nums[i];
                }
            }
            return sub.Count;
        }

        private int SearchInsert(List<int> nums, int target)
        {
            int lo = 0, hi = nums.Count - 1;
            while (lo <= hi)
            {
                int mid = (lo + hi) >> 1;
                if (target == nums[mid])
                {
                    return mid;
                }
                if (target > nums[mid])
                {
                    lo = mid + 1;
                }
                else
                {
                    hi = mid - 1;
                }
            }
            return lo;
        }
    }
}

/**
* A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. 
*   1. For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) alternate between positive and negative. 
*   2. In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences. 
*       The first is not because its first two differences are positive, and the second is not because its last difference is zero.
* A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.
* 
* A subsequence is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order. 
* Given an integer array nums, return the length of the longest wiggle subsequence of nums.
*/
using System;
using TestMain.Definitions;

namespace TestMain.DynamicProgramming
{
    class WiggleSubsequence : Solution
    {
        public override void Run()
        {
            AssertEqual(6, WiggleMaxLengthNaive(new int[] { 1, 7, 4, 9, 2, 5 }));
            AssertEqual(7, WiggleMaxLengthNaive(new int[] { 1, 17, 5, 10, 13, 15, 10, 5, 16, 8 }));
            AssertEqual(2, WiggleMaxLengthNaive(new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9 }));

            AssertEqual(6, WiggleMaxLengthConstant(new int[] { 1, 7, 4, 9, 2, 5 }));
            AssertEqual(7, WiggleMaxLengthConstant(new int[] { 1, 17, 5, 10, 13, 15, 10, 5, 16, 8 }));
            AssertEqual(2, WiggleMaxLengthConstant(new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9 }));
        }

        private int WiggleMaxLengthNaive(int[] nums)
        {
            // up[i] or down[i] is the max length of wiggle subsequences where last status is up or down.
            var up = new int[nums.Length];
            var down = new int[nums.Length];
            up[0] = 1;
            down[0] = 1;
            for (int i = 1; i < nums.Length; i++)
            {
                if (nums[i] > nums[i - 1])
                {
                    up[i] = down[i - 1] + 1;
                    down[i] = down[i - 1];
                }
                else if (nums[i] < nums[i - 1])
                {
                    down[i] = up[i - 1] + 1;
                    up[i] = up[i - 1];
                }
                else
                {
                    up[i] = up[i - 1];
                    down[i] = down[i - 1];
                }
            }
            return Math.Max(up[nums.Length - 1], down[nums.Length - 1]);
        }

        private int WiggleMaxLengthConstant(int[] nums)
        {
            int up = 1, down = 1;
            for (int i = 1; i < nums.Length; i++)
            {
                if (nums[i] > nums[i - 1])
                {
                    up = down + 1;
                }
                else if (nums[i] < nums[i - 1])
                {
                    down = up + 1;
                }
            }
            return Math.Max(up, down);
        }
    }
}

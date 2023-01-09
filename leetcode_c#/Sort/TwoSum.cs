/**
* Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 
* 
* You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.
*/
using System.Collections.Generic;
using TestMain.Definitions;

namespace TestMain.Sort
{
    class TwoSum : Solution
    {
        public override void Run()
        {
            AssertEqual(new int[] { 0, 1 }, TwoSumInternal(new int[] { 2, 7, 11, 15 }, 9));
            AssertEqual(new int[] { 1, 2 }, TwoSumInternal(new int[] { 3, 2, 4 }, 6));
            AssertEqual(new int[] { 0, 1 }, TwoSumInternal(new int[] { 3, 3 }, 6));
        }

        private int[] TwoSumInternal(int[] nums, int target)
        {
            var res = new int[2];
            var map = new Dictionary<int, int>();
            for (int i = 0; i < nums.Length; i++)
            {
                if (map.ContainsKey(target - nums[i]))
                {
                    res[0] = map[target - nums[i]];
                    res[1] = i;
                    break;
                }
                map[nums[i]] = i;
            }

            return res;
        }
    }
}

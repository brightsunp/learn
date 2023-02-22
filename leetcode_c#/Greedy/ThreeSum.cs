/**
* Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. 
* 
* Notice that the solution set must not contain duplicate triplets. The order of the output and the order of the triplets does not matter.
* 3 <= nums.length <= 3000, -10^5 <= nums[i] <= 10^5
*/
using System;
using System.Collections.Generic;
using TestMain.Definitions;

namespace TestMain.Greedy
{
    class ThreeSum : Solution
    {
        public override void Run()
        {
            AssertEqual(new List<IList<int>> { new int[] { -1, -1, 2 }, new int[] { -1, 0, 1 } }, ThreeSumInternal(new int[] { -1, 0, 1, 2, -1, -4 }));

            AssertEqual(2, ThreeSumClosest(new int[] { -1, 2, 1, -4 }, 1));
        }

        private IList<IList<int>> ThreeSumInternal(int[] nums)
        {
            Array.Sort(nums);
            var res = new List<IList<int>>();
            for (int i = 0; i < nums.Length; i++)
            {
                if (nums[i] > 0)
                {
                    break;
                }

                // Guarantee all the solutions are found to get target "-nums[i]".
                int lo = i + 1, hi = nums.Length - 1;
                while (lo < hi)
                {
                    int total = nums[lo] + nums[hi];
                    if (total == -nums[i])
                    {
                        res.Add(new int[] { nums[i], nums[lo], nums[hi] });

                        // Handle duplicates of num 2.
                        while (lo < hi && nums[lo] == nums[lo + 1])
                        {
                            lo++;
                        }

                        // Handle duplicates of num 3.
                        while (lo < hi && nums[hi] == nums[hi - 1])
                        {
                            hi--;
                        }

                        // Step forward to find other combinations.
                        lo++;
                        hi--;
                    }
                    else if (total > -nums[i])
                    {
                        hi--;
                    }
                    else
                    {
                        lo++;
                    }
                }

                // Handle duplicates of num 1.
                while (i + 1 < nums.Length && nums[i + 1] == nums[i])
                {
                    i++;
                }
            }
            
            return res;
        }

        // Given an integer array nums of length n and an integer target, return the sum of three integers in nums such that the sum is closest to target.
        // You may assume that each input would have exactly one solution.
        private int ThreeSumClosest(int[] nums, int target)
        {
            Array.Sort(nums);
            int res = nums[0] + nums[1] + nums[2];
            for (int i = 0; i < nums.Length; i++)
            {
                int lo = i + 1, hi = nums.Length - 1;
                while (lo < hi)
                {
                    int total = nums[i] + nums[lo] + nums[hi];
                    if (total == target)
                    {
                        return target;
                    }

                    if (Math.Abs(total - target) < Math.Abs(res - target))
                    {
                        res = total;
                    }
                    if (total < target)
                    {
                        lo++;
                    }
                    else
                    {
                        hi--;
                    }
                }
            }
            return res;
        }
    }
}

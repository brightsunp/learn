/**
* Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
* 
* 1 <= nums.length <= 200, 1 <= nums[i] <= 100
*/
using System.Collections.Generic;
using TestMain.Definitions;

namespace TestMain.DynamicProgramming
{
    class PartitionEqualSum : Solution
    {
        public override void Run()
        {
            AssertTrue(CanPartitionBacktrack(new int[] { 1, 5, 11, 5 }));
            AssertTrue(!CanPartitionBacktrack(new int[] { 1, 2, 3, 5 }));

            AssertTrue(CanPartitionDp(new int[] { 1, 5, 11, 5 }));
            AssertTrue(CanPartitionDp(new int[] { 3, 3, 3, 4, 5 }));
            AssertTrue(!CanPartitionDp(new int[] { 1, 2, 5 }));
            AssertTrue(!CanPartitionDp(new int[] { 1, 2, 3, 5 }));
        }

        // Figure out it's 0/1 knapsack problem: each number is picked up or not.
        private bool CanPartitionDp(int[] nums)
        {
            int sum = 0;
            foreach (int num in nums)
            {
                sum += num;
            }
            if ((sum & 1) == 1)
            {
                return false;
            }
            return CanPartitionDpRow(nums, sum >> 1);
        }

        // O(m*n) time and O(m*n) space
        private bool CanPartitionDpNaive(int[] nums, int target)
        {
            // dp[i, j] is whether sum j can be gotten from a subset of the first i numbers.
            bool[,] dp = new bool[nums.Length + 1, target + 1];

            // Initialization: consider sum([]) == 0
            for (int i = 0; i <= nums.Length; i++)
            {
                dp[i, 0] = true;
            }
            for (int j = 1; j <= target; j++)
            {
                dp[0, j] = false;
            }
            for (int i = 1; i <= nums.Length; i++)
            {
                for (int j = 1; j <= target; j++)
                {
                    dp[i, j] = dp[i - 1, j];
                    if (j >= nums[i - 1])
                    {
                        dp[i, j] |= dp[i - 1, j - nums[i - 1]];
                    }
                }
            }

            return dp[nums.Length, target];
        }

        // O(m*n) time and O(n) space
        private bool CanPartitionDpRow(int[] nums, int target)
        {
            // dp[i] is whether sum i can be gotten from a subset of nums.
            var dp = new bool[target + 1];
            dp[0] = true;

            foreach (int num in nums)
            {
                // Must be the inside loop, since appending new num will not affect previous results.
                // Must be top-down traverse, such that dp[i-num] has not considered num yet.
                for (int i = target; i >= num; i--)
                {
                    dp[i] |= dp[i - num];
                }
            }

            return dp[target];
        }

        // TLE, 36 / 141 testcases passed.
        private bool CanPartitionBacktrack(int[] nums)
        {
            int sum = 0;
            foreach (int num in nums)
            {
                sum += num;
            }
            if ((sum & 1) == 1)
            {
                return false;
            }
            var solutions = new List<List<int>>();
            Backtrack(nums, 0, new List<int>(), solutions, sum >> 1);
            return solutions.Count != 0;
        }

        private void Backtrack(int[] nums, int pos, List<int> solution, List<List<int>> solutions, int target)
        {
            if (target == 0)
            {
                solutions.Add(new List<int>(solution));
            }
            else
            {
                for (int i = pos; i < nums.Length; i++)
                {
                    if (target < nums[i])
                    {
                        continue;
                    }

                    solution.Add(nums[i]);
                    Backtrack(nums, i + 1, solution, solutions, target - nums[i]);
                    solution.RemoveAt(solution.Count - 1);
                }
            }
        }
    }
}

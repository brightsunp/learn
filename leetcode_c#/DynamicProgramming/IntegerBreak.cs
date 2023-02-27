/**
* Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers. 
* Return the maximum product you can get.
* 
* 2 <= n <= 58
*/
using System;
using TestMain.Definitions;

namespace TestMain.DynamicProgramming
{
    class IntegerBreak : Solution
    {
        public override void Run()
        {
            AssertEqual(1, IntegerBreakNaive(2));
            AssertEqual(36, IntegerBreakNaive(10));

            AssertEqual(1, IntegerBreakRow(2));
            AssertEqual(36, IntegerBreakRow(10));
        }

        private int IntegerBreakNaive(int n)
        {
            // dp[k, i] is the max product from k integers of which the sum is i.
            int subCount = (n >> 1) + 1;
            int[,] dp = new int[subCount + 1, n + 1];
            for (int i = 0; i <= n; i++)
            {
                dp[1, i] = i;
            }

            for (int k = 2; k <= subCount; k++)
            {
                for (int i = 2; i <= n; i++)
                {
                    for (int j = 1; j < i; j++)
                    {
                        dp[k, i] = Math.Max(dp[k, i], dp[k - 1, j] * (i - j));
                    }
                }
            }

            int res = int.MinValue;
            for (int k = 2; k <= subCount; k++)
            {
                res = Math.Max(res, dp[k, n]);
            }
            return res;
        }

        private int IntegerBreakRow(int n)
        {
            var dp = new int[n + 1];
            dp[1] = 1;
            for (int i = 2; i <= n; i++)
            {
                for (int j = 1; j <= (i >> 1); j++)
                {
                    // This is how to save the outer k loop!
                    // Math explanation: we have to compare i with dp[i] since the number can be further broken.
                    dp[i] = Math.Max(dp[i], Math.Max(j, dp[j]) * Math.Max(i - j, dp[i - j]));
                }
            }
            return dp[n];
        }
    }
}

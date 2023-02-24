/**
* A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. 
* For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
* 
* Given an integer n, return the least number of perfect square numbers that sum to n. 
*/
using System;
using TestMain.Definitions;

namespace TestMain.DynamicProgramming
{
    class PerfectSquares : Solution
    {
        public override void Run()
        {
            AssertEqual(3, NumSquares(12));
            AssertEqual(2, NumSquares(13));
        }

        private int NumSquares(int n)
        {
            var dp = new int[n + 1];
            for (int i = 1; i <= n; i++)
            {
                int res = int.MaxValue;
                for (int j = 1; j * j <= i; j++)
                {
                    res = Math.Min(res, dp[i - j * j] + 1);
                }
                dp[i] = res;
            }
            return dp[n];
        }
    }
}

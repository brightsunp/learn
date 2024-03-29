﻿/**
* Dynamic Programming is mainly an optimization over plain recursion: 
*   The idea is to simply store the results of sub-problems. Using extra space, it reduces time complexity from exponential to polynomial. 
*   Key point is to figure out the format of each sub problem, and formula between sub problems.
* 
*   "Someone may come up with O(1) space solution directly. But it's better to be generous when you think and be greedy when you implement."
*/
using TestMain.Definitions;

namespace TestMain.DynamicProgramming
{
    class FibonacciSeries : Solution
    {
        public override void Run()
        {
            var nums = new int[] { 0, 1, 1, 2, 3, 5, 8, 13 };
            for (int i = 0; i < nums.Length; i++)
            {
                AssertEqual(nums[i], Fibonacci(i));
                if (i < nums.Length - 1)
                {
                    AssertEqual(nums[i + 1], ClimbStairs(i));
                }
            }

            AssertEqual(2, DecodeWays("12"));
            AssertEqual(3, DecodeWays("226"));
            AssertEqual(0, DecodeWays("06"));
        }

        private int Fibonacci(int n)
        {
            if (n <= 1) return n;

            var dp = new int[n + 1];
            dp[0] = 0;
            dp[1] = 1;
            for (int i = 2; i <= n; i++)
            {
                dp[i] = dp[i - 1] + dp[i - 2];
            }
            return dp[n];
        }

        // You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps.
        // In how many distinct ways can you climb to the top?
        private int ClimbStairs(int n)
        {
            return Fibonacci(n + 1);
        }

        // Encode letter into number: 'A' -> "1", 'B' -> "2", ... 'Z' -> "26".
        // Given a string s containing only digits, return the number of ways to decode it. The length of s is in range [1, 100].
        //   Case: DecodeWays("11106") = 2;
        //   Explanation: the encoded message "11106" can be mapped into "AAJF"(1 1 10 6) or "KJF"(11 10 6). "06" is invalid!
        private int DecodeWays(string s)
        {
            if (s[0] == '0') return 0;

            var dp = new int[s.Length];
            dp[0] = 1;
            for (int i = 1; i < s.Length; i++)
            {
                // Handle the boundary cases carefully.
                if (s[i] == '0')
                {
                    if (s[i - 1] == '1' || s[i - 1] == '2')
                    {
                        if (i == 1)
                        {
                            dp[i] = 1;
                        }
                        else
                        {
                            dp[i] = dp[i - 2];
                        }
                    }
                    else
                    {
                        // Otherwise '0' cannot be decoded.
                        return 0;
                    }
                }
                else if (s[i - 1] == '1' || (s[i - 1] == '2' && s[i] <= '6'))
                {
                    if (i == 1)
                    {
                        dp[i] = 2;
                    }
                    else
                    {
                        // "Climbed" from i-1 or i-2 step.
                        dp[i] = dp[i - 1] + dp[i - 2];
                    }
                }
                else
                {
                    dp[i] = dp[i - 1];
                }
            }
            return dp[s.Length - 1];
        }
    }
}

/**
* You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money. 
*   I. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1. 
*   II. Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
* 
* You may assume that you have an infinite number of each kind of coin.
*/
using System;
using TestMain.Definitions;

namespace TestMain.DynamicProgramming
{
    class CoinChangeSeries : Solution
    {
        public override void Run()
        {
            AssertEqual(3, CoinChange(new int[] { 1, 2, 5 }, 11));
            AssertEqual(-1, CoinChange(new int[] { 2 }, 3));
            AssertEqual(0, CoinChange(new int[] { 1 }, 0));

            AssertEqual(1, CoinChangeII(new int[] { 1, 2, 5 }, 0));
            AssertEqual(4, CoinChangeII(new int[] { 1, 2, 5 }, 5));
            AssertEqual(0, CoinChangeII(new int[] { 2 }, 3));
            AssertEqual(1, CoinChangeII(new int[] { 10 }, 10));
        }

        // dp[i] is the fewest number of coins needed to make up amount i.
        private int CoinChange(int[] coins, int amount)
        {
            var dp = new int[amount + 1];
            dp[0] = 0;

            // This is different from 0/1 knapsnack problem which chooses to pick up each coin or not.
            for (int i = 1; i <= amount; i++)
            {
                dp[i] = int.MaxValue;
                foreach (int coin in coins)
                {
                    if (i >= coin && dp[i - coin] != int.MaxValue)
                    {
                        dp[i] = Math.Min(dp[i], 1 + dp[i - coin]);
                    }
                }
            }

            return dp[amount] == int.MaxValue ? -1 : dp[amount];
        }

        // dp[i] is the number of combinations that make up amount i.
        private int CoinChangeII(int[] coins, int amount)
        {
            var dp = new int[amount + 1];
            // Choosing no coins makes up the amount 0.
            dp[0] = 1;

            foreach (int coin in coins)
            {
                // Must be the inside loop, since previous combinations are unique and appending new type of coins will make them still unique.
                // Must be bottom-up traverse, such that dp[i-coin] has considered coin already. (top-down is the solution of using non-repeated coins)
                for (int i = coin; i <= amount; i++)
                {
                    dp[i] += dp[i - coin];
                }
            }

            return dp[amount];
        }
    }
}

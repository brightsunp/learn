/**
* You are given an array prices where prices[i] is the price of a given stock on the ith day. You can only hold at most one share of the stock at any time.
* I. You may choose a single day to buy one stock and a different day in the future to sell that stock.
* II. You may complete as many transactions as you like.
* III. You may complete at most two (or k) transactions.
* Plus II. After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
* Plus II. You need to pay the fee for each transaction.
* 
* Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0. 
* 1 <= prices.length <= 1000, 1 <= k <= 100.
*/
using System;
using TestMain.Definitions;

namespace TestMain.DynamicProgramming
{
    class StockSeries : Solution
    {
        public override void Run()
        {
            AssertEqual(5, MaxProfit(new int[] { 7, 1, 5, 3, 6, 4 }));
            AssertEqual(0, MaxProfit(new int[] { 7, 6, 4, 3, 1 }));

            AssertEqual(7, MaxProfitII(new int[] { 7, 1, 5, 3, 6, 4 }));
            AssertEqual(0, MaxProfitII(new int[] { 7, 6, 4, 3, 1 }));
            AssertEqual(4, MaxProfitII(new int[] { 1, 2, 3, 4, 5 }));

            AssertEqual(6, MaxProfitIII(new int[] { 3, 3, 5, 0, 0, 3, 1, 4 }));
            AssertEqual(0, MaxProfitIII(new int[] { 7, 6, 4, 3, 1 }));
            AssertEqual(4, MaxProfitIII(new int[] { 1, 2, 3, 4, 5 }));

            // [buy, sell, rest, buy, sell]
            AssertEqual(3, MaxProfitCooldown(new int[] { 1, 2, 3, 0, 2 }));

            AssertEqual(8, MaxProfitTransactionFee(new int[] { 1, 3, 2, 8, 4, 9 }, 2));
            AssertEqual(6, MaxProfitTransactionFee(new int[] { 1, 3, 7, 5, 10, 3 }, 3));
        }

        private int MaxProfit(int[] prices)
        {
            int curMin = prices[0], res = 0;
            for (int i = 1; i < prices.Length; i++)
            {
                res = Math.Max(res, prices[i] - curMin);
                curMin = Math.Min(curMin, prices[i]);
            }
            return res;
        }

        private int MaxProfitII(int[] prices)
        {
            int res = 0;
            for (int i = 1; i < prices.Length; i++)
            {
                res += Math.Max(prices[i] - prices[i - 1], 0);
            }
            return res;
        }

        private int MaxProfitIII(int[] prices)
        {
            // dp[k, i] is the max profit until prices[i] with at most k transactions.
            //  if not sold on prices[i], dp[k, i] = dp[k, i-1];
            //  if sold on prices[i], dp[k, i] = dp[k-1, j] + prices[i] - prices[j] where j is in [0, ..., i-1]
            //      whereas the sub-inner loop can be saved by updating a tmp variable.
            // If k >= (n>>1), the problem can be converted to MaxProfitII.
            int[,] dp = new int[3, prices.Length];
            for (int k = 1; k < 3; k++)
            {
                int tmpMax = dp[k - 1, 0] - prices[0];
                for (int i = 1; i < prices.Length; i++)
                {
                    dp[k, i] = Math.Max(dp[k, i - 1], tmpMax + prices[i]);
                    tmpMax = Math.Max(tmpMax, dp[k - 1, i] - prices[i]);
                }
            }

            return dp[2, prices.Length - 1];
        }

        private int MaxProfitCooldown(int[] prices)
        {
            // buy[i] is the max profit if the last non-rest action is buy.
            //  if buy on i-th day, buy[i] = sell[i-2] - prices[i-1];
            //  if rest on i-th day, buy[i] = buy[i-1]
            var buy = new int[prices.Length + 1];
            // sell[i] is the max profit if the last non-rest action is sell.
            //  if sell on i-th day, sell[i] = buy[i-1] + prices[i-1];
            //  if rest on i-th day, sell[i] = sell[i-1]
            var sell = new int[prices.Length + 1];
            buy[1] = -prices[0];
            for (int i = 2; i <= prices.Length; i++)
            {
                buy[i] = Math.Max(sell[i - 2] - prices[i - 1], buy[i - 1]);
                sell[i] = Math.Max(buy[i - 1] + prices[i - 1], sell[i - 1]);
            }

            return sell[prices.Length];
        }

        private int MaxProfitTransactionFee(int[] prices, int fee)
        {
            var buy = new int[prices.Length];
            var sell = new int[prices.Length];
            buy[0] = -prices[0];
            for (int i = 1; i < prices.Length; i++)
            {
                buy[i] = Math.Max(sell[i - 1] - prices[i], buy[i - 1]);
                sell[i] = Math.Max(buy[i - 1] + prices[i] - fee, sell[i - 1]);
            }

            return sell[prices.Length - 1];
        }
    }
}

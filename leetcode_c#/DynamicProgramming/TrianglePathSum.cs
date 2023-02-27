/**
* Given a triangle array, return the minimum path sum from top to bottom. 
* 
* For each step, you may move to an adjacent number of the row below. 
* More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
* 
* 1 <= triangle.length <= 200, triangle[0].length == 1, triangle[i].length == triangle[i - 1].length + 1, -10^4 <= triangle[i][j] <= 10^4
*/
using System;
using System.Collections.Generic;
using TestMain.Definitions;

namespace TestMain.DynamicProgramming
{
    class TrianglePathSum : Solution
    {
        public override void Run()
        {
            /*
            *    2
            *   3 4
            *  6 5 7
            * 4 1 8 3
            */
            var test = new List<IList<int>> { new List<int> { 2 }, new List<int> { 3, 4 }, new List<int> { 6, 5, 7 }, new List<int> { 4, 1, 8, 3 } };
            AssertEqual(11, TriangleNaive(test));
            AssertEqual(11, TriangleRows(test));
        }

        private int TriangleNaive(IList<IList<int>> triangle)
        {
            // dp[i][j] = Math.Min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
            var dp = new int[triangle.Count][];
            for (int i = 0; i < triangle.Count; i++)
            {
                dp[i] = new int[i + 1];
            }
            dp[0][0] = triangle[0][0];

            for (int i = 1; i < triangle.Count; i++)
            {
                dp[i][0] = dp[i - 1][0] + triangle[i][0];
                for (int j = 1; j < i + 1; j++)
                {
                    int preMin = dp[i - 1][j - 1];
                    if (j < i && dp[i - 1][j] < preMin)
                    {
                        preMin = dp[i - 1][j];
                    }
                    dp[i][j] = preMin + triangle[i][j];
                }
            }

            int res = int.MaxValue;
            foreach (int val in dp[triangle.Count - 1])
            {
                res = Math.Min(res, val);
            }
            return res;
        }

        private int TriangleRows(IList<IList<int>> triangle)
        {
            var preRow = new int[triangle.Count];
            var curRow = new int[triangle.Count];
            preRow[0] = triangle[0][0];
            curRow[0] = triangle[0][0];

            for (int i = 1; i < triangle.Count; i++)
            {
                curRow[0] = preRow[0] + triangle[i][0];
                for (int j = 1; j < i + 1; j++)
                {
                    int preMin = preRow[j - 1];
                    if (j < i && preRow[j] < preMin)
                    {
                        preMin = preRow[j];
                    }
                    curRow[j] = preMin + triangle[i][j];
                }
                for (int j = 0; j < i + 1; j++)
                {
                    preRow[j] = curRow[j];
                }
            }

            int res = int.MaxValue;
            foreach (int val in curRow)
            {
                res = Math.Min(res, val);
            }
            return res;
        }
    }
}

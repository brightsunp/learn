/**
* There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
* The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time. 
* Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
*/
using TestMain.Definitions;
using TestMain.Snippets;

namespace TestMain.DynamicProgramming
{
    class UniquePaths : Solution
    {
        public override void Run()
        {
            AssertEqual(1, UniquePathsNative(1, 1));
            AssertEqual(3, UniquePathsNative(3, 2));
            AssertEqual(28, UniquePathsNative(3, 7));

            AssertEqual(28, UniquePathsRows(3, 7));
            AssertEqual(28, UniquePathsRow(3, 7));
        }

        // O(m*n) time and O(m*n) space
        private int UniquePathsNative(int m, int n)
        {
            int[,] dp = new int[m, n];
            for (int i = 0; i < m; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    dp[i, j] = 1;
                }
            }

            for (int i = 1; i < m; i++)
            {
                for (int j = 1; j < n; j++)
                {
                    dp[i, j] = dp[i - 1, j] + dp[i, j - 1];
                }
            }

            return dp[m - 1, n - 1];
        }

        // O(m*n) time and O(n) space
        private int UniquePathsRows(int m, int n)
        {
            var preRow = new int[n];
            preRow.Populate(1);
            var curRow = new int[n];
            curRow.Populate(1);

            for (int i = 1; i < m; i++)
            {
                for (int j = 1; j < n; j++)
                {
                    curRow[j] = preRow[j] + curRow[j - 1];
                }
                for (int j = 0; j < n; j++)
                {
                    preRow[j] = curRow[j];
                }
            }
            return curRow[n - 1];
        }

        // O(m*n) time and O(n) space
        private int UniquePathsRow(int m, int n)
        {
            var row = new int[n];
            row.Populate(1);

            for (int i = 1; i < m; i++)
            {
                for (int j = 1; j < n; j++)
                {
                    row[j] += row[j - 1];
                }
            }
            return row[n - 1];
        }
    }
}

/**
* There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
* The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time. 
* 
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
            AssertEqual(1, UniquePathsNaive(1, 1));
            AssertEqual(3, UniquePathsNaive(3, 2));
            AssertEqual(28, UniquePathsNaive(3, 7));

            AssertEqual(28, UniquePathsRows(3, 7));
            AssertEqual(28, UniquePathsRow(3, 7));

            AssertEqual(7, MinPathSum(new int[][] { new int[] { 1, 3, 1 }, new int[] { 1, 5, 1 }, new int[] { 4, 2, 1 } }));
            AssertEqual(12, MinPathSum(new int[][] { new int[] { 1, 2, 3 }, new int[] { 4, 5, 6 } }));
        }

        // O(m*n) time and O(m*n) space.
        private int UniquePathsNaive(int m, int n)
        {
            int[,] dp = new int[m, n];
            for (int i = 0; i < m; i++)
            {
                dp[i, 0] = 1;
            }
            for (int j = 1; j < n; j++)
            {
                dp[0, j] = 1;
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

        // O(m*n) time and O(n) space.
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

                // Replace preRow values with curRow.
                for (int j = 0; j < n; j++)
                {
                    preRow[j] = curRow[j];
                }
            }
            return curRow[n - 1];
        }

        // O(m*n) time and O(n) space, not straightforward to understand.
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

        private int MinPathSum(int[][] grid)
        {
            int m = grid.Length, n = grid[0].Length;
            int[,] dp = new int[m, n];
            dp[0, 0] = grid[0][0];
            for (int i = 1; i < m; i++)
            {
                dp[i, 0] = dp[i - 1, 0] + grid[i][0];
            }
            for (int j = 1; j < n; j++)
            {
                dp[0, j] = dp[0, j - 1] + grid[0][j];
            }

            for (int i = 1; i < m; i++)
            {
                for (int j = 1; j < n; j++)
                {
                    dp[i, j] = System.Math.Min(dp[i - 1, j], dp[i, j - 1]) + grid[i][j];
                }
            }
            return dp[m - 1, n - 1];
        }
    }
}

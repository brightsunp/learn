/**
* You are given an m x n integer matrix matrix with the following two properties: 
*   1. Integers in each row are sorted in ascending from left to right.
*   2. The first integer of each row is greater than the last integer of the previous row. 
*   
* Given an integer target, return true if target is in matrix or false otherwise. 
* You must write a solution in O(log(m * n)) time complexity.
* 
* m == matrix.length, n == matrix[i].length, 1 <= m, n <= 100
*/
using TestMain.Definitions;

namespace TestMain.Search
{
    class SearchMatrix : Solution
    {
        public override void Run()
        {
            AssertTrue(SearchMatrixInternal(new int[][] { new int[] { 1, 3, 5, 7 }, new int[] { 10, 11, 16, 20 }, new int[] { 23, 30, 34, 60 } }, 3));
            AssertTrue(!SearchMatrixInternal(new int[][] { new int[] { 1, 3, 5, 7 }, new int[] { 10, 11, 16, 20 }, new int[] { 23, 30, 34, 60 } }, 13));

            AssertTrue(SearchMatrixII(new int[][] { new int[] { 1, 4, 7, 11, 15 }, new int[] { 2, 5, 8, 12, 19 }, new int[] { 3, 6, 9, 16, 22 }, 
                new int[] { 10, 13, 14, 17, 24 }, new int[] { 18, 21, 23, 26, 30 } }, 5));
            AssertTrue(!SearchMatrixII(new int[][] { new int[] { 1, 4, 7, 11, 15 }, new int[] { 2, 5, 8, 12, 19 }, new int[] { 3, 6, 9, 16, 22 },
                new int[] { 10, 13, 14, 17, 24 }, new int[] { 18, 21, 23, 26, 30 } }, 20));
        }

        private bool SearchMatrixInternal(int[][] matrix, int target)
        {
            // Just do the binary search in a "flattened" array.
            int m = matrix.Length, n = matrix[0].Length;
            int lo = 0, hi = m * n - 1;
            while (lo <= hi)
            {
                int mid = (lo + hi) >> 1;
                int x = mid / n, y = mid % n;
                if (target == matrix[x][y])
                {
                    return true;
                }
                else if (target < matrix[x][y])
                {
                    hi = mid - 1;
                }
                else
                {
                    lo = mid + 1;
                }
            }
            return false;
        }

        // Property 2: Integers in each column are sorted in ascending from top to bottom.
        // O(m + n) time, searching from top-right or bottom-left.
        private bool SearchMatrixII(int[][] matrix, int target)
        {
            int m = matrix.Length, n = matrix[0].Length;
            int row = m - 1, col = 0;
            while (row >= 0 && col < n)
            {
                if (target == matrix[row][col])
                {
                    return true;
                }
                if (target < matrix[row][col])
                {
                    row--;
                }
                else
                {
                    col++;
                }
            }
            return false;
        }
    }
}

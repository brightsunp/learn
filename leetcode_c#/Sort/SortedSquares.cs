/**
* Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
*/
using TestMain.Definitions;

namespace TestMain.Sort
{
    class SortedSquares : Solution
    {
        public override void Run()
        {
            AssertEqual(new int[] { 0, 1, 9, 16, 100 }, SortedSquaresInternal(new int[] { -4, -1, 0, 3, 10 }));
            AssertEqual(new int[] { 4, 9, 9, 49, 121 }, SortedSquaresInternal(new int[] { -7, -3, 2, 3, 11 }));
        }

        private int[] SortedSquaresInternal(int[] nums)
        {
            // merge sort!
            // and no need to find last negative index!
            var res = new int[nums.Length];
            int lo = 0, hi = nums.Length - 1, k = nums.Length - 1;
            while (k >= 0)
            {
                int cur1 = nums[lo] * nums[lo], cur2 = nums[hi] * nums[hi];
                if (cur1 > cur2)
                {
                    res[k--] = cur1;
                    lo++;
                }
                else
                {
                    res[k--] = cur2;
                    hi--;
                }
            }
            return res;

            /*
            int lastNegativeIndex = -1;
            foreach (int num in nums)
            {
                if (num >= 0)
                {
                    break;
                }
                lastNegativeIndex++;
            }
            int i = lastNegativeIndex, j = lastNegativeIndex + 1, k = 0;
            while (i >= 0 && j < nums.Length)
            {
                int curI = nums[i] * nums[i], curJ = nums[j] * nums[j];
                if (curI < curJ)
                {
                    res[k++] = curI;
                    i--;
                }
                else
                {
                    res[k++] = curJ;
                    j++;
                }
            }
            while (i >= 0)
            {
                res[k++] = nums[i] * nums[i];
                i--;
            }
            while (j < nums.Length)
            {
                res[k++] = nums[j] * nums[j];
                j++;
            }
            return res;
            */
        }
    }
}

/**
* Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].
*/
using TestMain.Definitions;
using System.Collections.Generic;

namespace TestMain.Sort
{
    class CountSmaller : Solution
    {
        private int[] counter;

        public override void Run()
        {
            var expected = new int[] { 2, 1, 1, 0 };
            var actual = new int[] { 5, 2, 6, 1 };
            AssertEqual(expected, CountStraightforward(actual));

            actual = new int[] { 5, 2, 6, 1 };
            AssertEqual(expected, CountInsertionSort(actual));

            actual = new int[] { 5, 2, 6, 1 };
            AssertEqual(expected, CountMergeSort(actual));
        }

        // Brutal force: O(n*n)
        private IList<int> CountStraightforward(int[] nums)
        {
            var res = new int[nums.Length];
            for (int i = 0; i < nums.Length; i++)
            {
                for (int j = i + 1; j < nums.Length; j++)
                {
                    if (nums[j] < nums[i])
                    {
                        res[i]++;
                    }
                }
            }
            return res;
        }

        // TLE since the worst case is O(n*n)
        private IList<int> CountInsertionSort(int[] nums)
        {
            var res = new int[nums.Length];
            for (int i = nums.Length - 1; i >= 0; i--)
            {
                int j = i + 1, cur = nums[i];
                while (j <= nums.Length - 1 && cur > nums[j])
                {
                    nums[j - 1] = nums[j];
                    j++;
                }
                nums[j - 1] = cur;
                res[i] = j - 1 - i;
            }
            return res;
        }

        // The smaller numbers on the right of a number, are exactly those that jump from its right to its left during a stable sort.
        // Tricky part is tracking the numbers' new indexes during the merge process.
        // When right element is merged, increase the right count; when left element is merged, update the count result.
        private IList<int> CountMergeSort(int[] nums)
        {
            counter = new int[nums.Length];
            var indexes = new int[nums.Length];
            for (int i = 0; i < nums.Length; i++)
            {
                indexes[i] = i;
            }
            MergeSort(nums, indexes, 0, nums.Length - 1);
            return counter;
        }

        private void MergeSort(int[] nums, int[] indexes, int left, int right)
        {
            if (left == right)
            {
                return;
            }
            int mid = (left + right) >> 1;
            MergeSort(nums, indexes, left, mid);
            MergeSort(nums, indexes, mid + 1, right);
            Merge(nums, indexes, left, mid, right);
        }

        private void Merge(int[] nums, int[] indexes, int left, int mid, int right)
        {
            var tmpIndexes = new int[right - left + 1];
            int rightCount = 0, k = 0, i = left, j = mid + 1;
            while (i <= mid && j <= right)
            {
                // Only use nums for comparision
                if (nums[indexes[i]] > nums[indexes[j]])
                {
                    rightCount++;
                    tmpIndexes[k++] = indexes[j++];
                }
                else
                {
                    counter[indexes[i]] += rightCount;
                    tmpIndexes[k++] = indexes[i++];
                }
            }
            while (i <= mid)
            {
                // Do not forget
                counter[indexes[i]] += rightCount;
                tmpIndexes[k++] = indexes[i++];
            }
            while (j <= right)
            {
                tmpIndexes[k++] = indexes[j++];
            }
            for (int m = left; m <= right; m++)
            {
                indexes[m] = tmpIndexes[m - left];
            }
        }
    }
}

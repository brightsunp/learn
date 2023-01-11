using System;
using System.Linq;

namespace TestMain.Snippets
{
    static class Array
    {
        // Repeatedly swap the adjacent elements if they are in wrong order.
        public static void BubbleSort(this int[] nums)
        {
            for (int i = 0; i < nums.Length; i++)
            {
                bool didSwap = false;
                for (int j = i + 1; j < nums.Length; j++)
                {
                    if (nums[j] < nums[j - 1])
                    {
                        Swap(nums, j, j - 1);
                        didSwap = true;
                    }
                }

                // It means all the remaining elements are in correct order, which gets O(n) for the best case.
                if (!didSwap)
                {
                    return;
                }
            }
        }

        // Repeatedly find the minimum element and swap it with the beginning.
        public static void SelectionSort(this int[] nums)
        {
            for (int i = 0; i < nums.Length; i++)
            {
                int minIndex = i;
                for (int j = i + 1; j < nums.Length; j++)
                {
                    if (nums[j] < nums[minIndex])
                    {
                        minIndex = j;
                    }
                }
                Swap(nums, minIndex, i);
            }
        }

        // Repeatedly insert current element to the correct position.
        public static void InsertionSort(this int[] nums)
        {
            for (int i = 1; i < nums.Length; i++)
            {
                int j = i - 1, cur = nums[i];
                while (j >= 0 && cur < nums[j])
                {
                    nums[j + 1] = nums[j];
                    j--;
                }
                nums[j + 1] = cur;
            }
        }

        // Divide into two equal halves and combine them in a sorted manner. Requires O(N) extra storage.
        public static void MergeSort(this int[] nums)
        {
            MergeSortInternal(nums, 0, nums.Length - 1);
        }

        // Pick an element x as a pivot and partition the elements to smaller than x and greater than x.
        public static void QuickSort(this int[] nums)
        {
            QuickSortInternal(nums, 0, nums.Length - 1);
        }

        // Apply to elements where the range is not significantly greater than the total count.
        public static void CountingSort(this int[] nums)
        {
            int maxValue = nums.Max(), minValue = nums.Min();
            var count = new int[maxValue - minValue + 1];
            for (int i = 0; i < nums.Length; i++)
            {
                count[nums[i] - minValue]++;
            }
            int j = 0;
            for (int i = 0; i < count.Length; i++)
            {
                while (count[i] > 0)
                {
                    nums[j++] = i + minValue;
                    count[i]--;
                }
            }
        }

        public static int BinarySearch(this int[] sortedNums, int target)
        {
            int lo = 0, hi = sortedNums.Length - 1;
            while (lo <= hi)
            {
                int mid = (lo + hi) >> 1;
                if (target == sortedNums[mid])
                {
                    return mid;
                }
                
                if (target < sortedNums[mid])
                {
                    hi = mid - 1;
                }
                else
                {
                    lo = mid + 1;
                }
            }

            return -1;
        }

        public static int[] SampleActual()
        {
            return new int[] { 5, 1, 4, 2, 8 };
        }

        public static int[] SampleExpected()
        {
            return new int[] { 1, 2, 4, 5, 8 };
        }

        private static void Swap(int[] nums, int i, int j)
        {
            int tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
        }

        private static void MergeSortInternal(int[] nums, int lo, int hi)
        {
            if (lo >= hi)
            {
                return;
            }

            int mid = (lo + hi) >> 1;
            MergeSortInternal(nums, lo, mid);
            MergeSortInternal(nums, mid + 1, hi);
            Merge(nums, lo, mid, hi);
        }

        private static void Merge(int[] nums, int lo, int mid, int hi)
        {
            var tmp = new int[hi - lo + 1];
            int k = 0, i = lo, j = mid + 1;
            while (i <= mid && j <= hi)
            {
                if (nums[i] < nums[j])
                {
                    tmp[k++] = nums[i++];
                }
                else
                {
                    tmp[k++] = nums[j++];
                }
            }
            while (i <= mid)
            {
                tmp[k++] = nums[i++];
            }
            while (j <= hi)
            {
                tmp[k++] = nums[j++];
            }

            for (int m = 0; m < tmp.Length; m++)
            {
                nums[m + lo] = tmp[m];
            }
        }

        private static void QuickSortInternal(int[] nums, int lo, int hi)
        {
            if (lo >= hi)
            {
                return;
            }

            int pi = Partition(nums, lo, hi);
            QuickSortInternal(nums, lo, pi - 1);
            QuickSortInternal(nums, pi + 1, hi);
        }

        private static int Partition(int[] nums, int lo, int hi)
        {
            // Practically, picking random index has expected O(n*logn) time complexity.
            int pi = new Random().Next(lo, hi + 1);
            Swap(nums, pi, hi);

            int pivot = nums[hi], i = lo;
            for (int j = lo; j < hi; j++)
            {
                if (nums[j] < pivot)
                {
                    Swap(nums, i, j);
                    i++;
                }
            }
            Swap(nums, i, hi);

            return i;
        }
    }
}

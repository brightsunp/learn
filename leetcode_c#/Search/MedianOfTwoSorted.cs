/**
* Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
* The overall run time complexity should be O(log (m+n)).
*/
using System;
using TestMain.Definitions;

namespace TestMain.Search
{
    class MedianOfTwoSorted : Solution
    {
        public override void Run()
        {
            AssertEqual((double)2, FindMedianMerge(new int[] { 1, 3 }, new int[] { 2 }));
            AssertEqual((double)2.5, FindMedianMerge(new int[] { 1, 3 }, new int[] { 2, 4 }));

            AssertEqual((double)2, FindMedianPartition(new int[] { 1, 3 }, new int[] { 2 }));
            AssertEqual((double)2.5, FindMedianPartition(new int[] { 1, 3 }, new int[] { 2, 4 }));
        }

        // Straightforward: merge and find median - O(m+n), can dismiss space complexity though.
        private double FindMedianMerge(int[] nums1, int[] nums2)
        {
            var res = new int[nums1.Length + nums2.Length];
            int i = 0, j = 0, k = 0;
            while (i < nums1.Length && j < nums2.Length)
            {
                if (nums1[i] < nums2[j])
                {
                    res[k++] = nums1[i++];
                }
                else
                {
                    res[k++] = nums2[j++];
                }
            }
            while (i < nums1.Length)
            {
                res[k++] = nums1[i++];
            }
            while (j < nums2.Length)
            {
                res[k++] = nums2[j++];
            }

            int L = (k - 1) >> 1, R = k >> 1;
            return (res[L] + res[R]) / 2.0;
        }

        // Leverage math definition of median: partition across two arrays - O(log (m+n)).
        private double FindMedianPartition(int[] nums1, int[] nums2)
        {
            if (nums1.Length > nums2.Length)
            {
                return FindMedianPartition(nums2, nums1);
            }

            int m = nums1.Length, n = nums2.Length, lo = 0, hi = nums1.Length;
            while (lo <= hi)
            {
                int partitionX = (lo + hi) >> 1;
                // Operator priority: bit is lower than plus
                int partitionY = ((m + n + 1) >> 1) - partitionX;

                // Get maxLeftX, minRightX, maxLeftY, minRightY respectively
                // Assign MinValue/MaxValue for edge cases since they are only used for value comparision
                int maxLeftX = partitionX == 0 ? int.MinValue : nums1[partitionX - 1];
                int minRightX = partitionX == m ? int.MaxValue : nums1[partitionX];
                int maxLeftY = partitionY == 0 ? int.MinValue : nums2[partitionY - 1];
                int minRightY = partitionY == n ? int.MaxValue : nums2[partitionY];

                if (maxLeftX <= minRightY && maxLeftY <= minRightX)
                {
                    // Reach the targeted partition
                    if ((m + n) % 2 == 0)
                    {
                        return (Math.Max(maxLeftX, maxLeftY) + Math.Min(minRightX, minRightY)) / 2.0;
                    }
                    else
                    {
                        return Math.Max(maxLeftX, maxLeftY);
                    }
                }
                else if (maxLeftX > minRightY)
                {
                    hi = partitionX - 1;
                }
                else
                {
                    lo = partitionX + 1;
                }
            }

            throw new Exception("The input arrays are not sorted!");
        }
    }
}

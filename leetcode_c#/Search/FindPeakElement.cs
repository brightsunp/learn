/**
* A peak element is an element that is strictly greater than its neighbors. You may imagine that nums[-1] = nums[n] = -∞. 
* 
* Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks. 
* You must write an algorithm that runs in O(log n) time.
* 
* 1 <= nums.length <= 1000, nums[i] != nums[i + 1] for all valid i.
*/
using TestMain.Definitions;

namespace TestMain.Search
{
    class FindPeakElement : Solution
    {
        public override void Run()
        {
            AssertEqual(2, FindPeak(new int[] { 1, 2, 3, 1 }));
            AssertEqual(5, FindPeak(new int[] { 1, 2, 1, 3, 5, 6, 4 }));
        }

        // Why the unsorted array problem can be solved using binary search:
        //  1. Hold the invariant: nums[left - 1] < nums[left] && nums[right] > nums[right + 1];
        //      a) if left -> decreasing, then left is a peak;
        //      b) if left -> increasing -> right, then right is a peak;
        //      c) if left -> increasing -> ... -> decreasing, then the point just before it starts decreasing is a peak.
        //  2. Reduce searching range: choose the subarray which respects the invariant.
        private int FindPeak(int[] nums)
        {
            int lo = 0, hi = nums.Length - 1;
            while (lo < hi)
            {
                int mid = (lo + hi) >> 1;
                if (nums[mid] < nums[mid + 1])
                {
                    lo = mid + 1;
                }
                else
                {
                    // Note the non-equal part is given from the problem.
                    hi = mid;
                }
            }
            return lo;
        }
    }
}

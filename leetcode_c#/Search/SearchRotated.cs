/**
* There is an integer array nums sorted in ascending order (with distinct values). 
* Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
* For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2]. 
* 
* Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums. 
* You must write an algorithm with O(log n) runtime complexity.
*/
using TestMain.Definitions;

namespace TestMain.Search
{
    class SearchRotated : Solution
    {
        public override void Run()
        {
            AssertEqual(2, Search(new int[] { 4, 5, 6, 7, 0, 1, 2 }, 6));
            AssertEqual(3, Search(new int[] { 2, 4, 5, 6, 7, 0, 1 }, 6));
            AssertEqual(4, Search(new int[] { 1, 2, 4, 5, 6, 7, 0 }, 6));
            AssertEqual(5, Search(new int[] { 0, 1, 2, 4, 5, 6, 7 }, 6));
            AssertEqual(6, Search(new int[] { 7, 0, 1, 2, 4, 5, 6 }, 6));
            AssertEqual(0, Search(new int[] { 6, 7, 0, 1, 2, 4, 5 }, 6));
            AssertEqual(1, Search(new int[] { 5, 6, 7, 0, 1, 2, 4 }, 6));

            AssertEqual(2, SearchWithVirtualIndex(new int[] { 4, 5, 6, 7, 0, 1, 2 }, 6));
            AssertEqual(3, SearchWithVirtualIndex(new int[] { 2, 4, 5, 6, 7, 0, 1 }, 6));
            AssertEqual(4, SearchWithVirtualIndex(new int[] { 1, 2, 4, 5, 6, 7, 0 }, 6));
            AssertEqual(5, SearchWithVirtualIndex(new int[] { 0, 1, 2, 4, 5, 6, 7 }, 6));
            AssertEqual(6, SearchWithVirtualIndex(new int[] { 7, 0, 1, 2, 4, 5, 6 }, 6));
            AssertEqual(0, SearchWithVirtualIndex(new int[] { 6, 7, 0, 1, 2, 4, 5 }, 6));
            AssertEqual(1, SearchWithVirtualIndex(new int[] { 5, 6, 7, 0, 1, 2, 4 }, 6));
        }

        private int Search(int[] nums, int target)
        {
            int lo = 0, hi = nums.Length - 1;
            while (lo <= hi)
            {
                int mid = (lo + hi) >> 1;
                if (nums[mid] == target)
                {
                    return mid;
                }

                if (nums[mid] > nums[hi])
                {
                    if (target >= nums[lo] && target < nums[mid])
                    {
                        hi = mid - 1;
                    }
                    else
                    {
                        lo = mid + 1;
                    }
                }
                else
                {
                    if (target <= nums[hi] && target > nums[mid])
                    {
                        lo = mid + 1;
                    }
                    else
                    {
                        hi = mid - 1;
                    }
                }
            }

            return -1;
        }

        private int SearchWithVirtualIndex(int[] nums, int target)
        {
            int lo = 0, hi = nums.Length - 1;
            // find the rotated index
            while (lo < hi)
            {
                int mid = (lo + hi) >> 1;
                if (nums[mid] < nums[hi])
                {
                    hi = mid;
                }
                else
                {
                    lo = mid + 1;
                }
            }

            int left = lo, right = nums.Length + lo;
            while (left < right)
            {
                int mid = (left + right) >> 1;
                int realMid = mid % nums.Length;
                if (nums[realMid] == target)
                {
                    return realMid;
                }

                if (nums[realMid] > target)
                {
                    right = mid;
                }
                else
                {
                    left = mid + 1;
                }
            }

            return -1;
        }
    }
}

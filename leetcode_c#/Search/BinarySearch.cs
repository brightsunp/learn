/**
* Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
* If target exists, then return its index. Otherwise, return -1.
* You must write an algorithm with O(log n) runtime complexity.
*/
using TestMain.Definitions;

namespace TestMain.Search
{
    class BinarySearch : Solution
    {
        public override void Run()
        {
            AssertEqual(4, BinarySearchInternal(new int[] { -1, 0, 3, 5, 9, 12 }, 9));
            AssertEqual(-1, BinarySearchInternal(new int[] { -1, 0, 3, 5, 9, 12 }, 2));
        }

        private int BinarySearchInternal(int[] nums, int target)
        {
            int lo = 0, hi = nums.Length - 1;
            while (lo <= hi)
            {
                int mid = (lo + hi) >> 1;
                if (target == nums[mid])
                {
                    return mid;
                }

                if (target < nums[mid])
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
    }
}

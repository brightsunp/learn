/**
* Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
* 
* 1 <= nums.length <= 1000, 0 <= nums[i] <= 1000
*/
using TestMain.Definitions;

namespace TestMain.Greedy
{
    class TriangleNumber : Solution
    {
        public override void Run()
        {
            AssertEqual(3, TriangleNumberInternal(new int[] { 2, 2, 3, 4 }));
            AssertEqual(4, TriangleNumberInternal(new int[] { 4, 2, 3, 4 }));
        }

        private int TriangleNumberInternal(int[] nums)
        {
            System.Array.Sort(nums);
            int res = 0;
            for (int k = nums.Length - 1; k >= 2; k--)
            {
                int i = 0, j = k - 1;
                while (i < j)
                {
                    if (nums[i] + nums[j] > nums[k])
                    {
                        res += j - i;
                        j--;
                    }
                    else
                    {
                        i++;
                    }
                }
            }
            return res;
        }
    }
}

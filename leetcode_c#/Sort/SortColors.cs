/**
* Given an array nums with n objects colored red, white, or blue, 
* sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
* 
* We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
* You must solve this problem without using the library's sort function.
*/
using TestMain.Definitions;

namespace TestMain.Sort
{
    class SortColors : Solution
    {
        public override void Run()
        {
            var expected = new int[] { 0, 0, 1, 1, 2, 2 };
            var actual = new int[] { 2, 0, 2, 1, 1, 0 };
            SortCounting(actual);
            AssertEqual(expected, actual);
        }
        
        private void SortCounting(int[] nums)
        {
            var count = new int[3];
            for (int i = 0; i < nums.Length; i++)
            {
                count[nums[i]]++;
            }
            int j = 0;
            for (int i = 0; i < 3; i++)
            {
                while (count[i] > 0)
                {
                    nums[j++] = i;
                    count[i]--;
                }
            }
        }
    }
}

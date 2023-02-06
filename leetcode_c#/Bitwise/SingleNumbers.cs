/**
* Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
* You must implement a solution with a linear runtime complexity and use only constant extra space.
* 
* Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. 
* You can return the answer in any order. You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.
*/
using TestMain.Definitions;

namespace TestMain.Bitwise
{
    class SingleNumbers : Solution
    {
        public override void Run()
        {
            AssertEqual(new int[] { 5, 3 }, SingleNumberIII(new int[] { 1, 2, 1, 3, 2, 5 }));
            AssertEqual(2, SingleNumberII(new int[] { 1, 2, 4, 1, 4, 4, 1 }));
        }

        private int SingleNumberII(int[] nums)
        {
            int once = 0, twice = 0;
            foreach (int num in nums)
            {
                // Adding num to set once if num is not in set twice.
                once = (once ^ num) & (~twice);
                // Adding num to set twice if num is not in set once.
                twice = (twice ^ num) & (~once);
            }
            return once;
        }

        private int[] SingleNumberIII(int[] nums)
        {
            int diff = 0;
            foreach(int num in nums)
            {
                diff ^= num;
            }
            // Get binary number containing the rightmost set bit.
            diff &= ~(diff - 1);

            var res = new int[2];
            foreach(int num in nums)
            {
                if ((num & diff) == 0)
                {
                    res[0] ^= num;
                }
                else
                {
                    res[1] ^= num;
                }
            }
            return res;
        }
    }
}

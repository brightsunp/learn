using TestMain.Definitions;

namespace TestMain.Bitwise
{
    class SingleNumbers : Solution
    {
        public override void Run()
        {
            AssertEqual(3, MissingNumber(new int[] { 1, 0, 2 }));
            AssertEqual(2, MissingNumber(new int[] { 0, 1, 3 }));
            AssertEqual(2, SingleNumber(new int[] { 0, 1, 3, 1, 3, 2, 0 }));

            AssertEqual(new int[] { 5, 3 }, SingleNumberIII(new int[] { 1, 2, 1, 3, 2, 5 }));
            AssertEqual(2, SingleNumberII(new int[] { 1, 2, 4, 1, 4, 4, 1 }));
        }

        // Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
        private int MissingNumber(int[] nums)
        {
            // If not any missing [0, n), return n; if any missing [0, n), n must be there, convert to SingleNumber.
            int res = nums.Length;
            for (int i = 0; i < nums.Length; i++)
            {
                res ^= (i ^ nums[i]);
            }
            return res;
        }

        // Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
        private int SingleNumber(int[] nums)
        {
            int res = 0;
            foreach (int num in nums)
            {
                res ^= num;
            }
            return res;
        }

        // Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
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

        // Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice.Find the two elements that appear only once.
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

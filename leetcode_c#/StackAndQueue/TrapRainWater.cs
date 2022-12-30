/**
* Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
*/
using TestMain.Definitions;

namespace TestMain.StackAndQueue
{
    class TrapRainWater : Solution
    {
        public override void Run()
        {
            var test1 = new int[] { 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 };
            AssertEqual(6, Trap(test1));

            var test2 = new int[] { 4, 2, 0, 3, 2, 5 };
            AssertEqual(9, Trap(test2));
        }

        // Must find the formula:
        // currentHolder = max(0, min(leftMaxHeight, rightMaxHeight) - currentHeight);
        private int Trap(int[] height)
        {
            int res = 0, leftMax = 0, rightMax = 0, left = 0, right = height.Length - 1;
            while (left <= right)
            {
                // leftMax is less than rightMax
                if (height[left] < height[right])
                {
                    // then compare leftMax and current
                    if (height[left] > leftMax)
                    {
                        leftMax = height[left];
                    }
                    else
                    {
                        res += leftMax - height[left];
                    }
                    left += 1;
                }
                else
                {
                    if (height[right] > rightMax)
                    {
                        rightMax = height[right];
                    }
                    else
                    {
                        res += rightMax - height[right];
                    }
                    right -= 1;
                }
            }

            return res;
        }
    }
}

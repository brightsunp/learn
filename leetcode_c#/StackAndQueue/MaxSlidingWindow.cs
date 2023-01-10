/**
* You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
* Each time the sliding window moves right by one position, you get a max value of the k numbers. Return all the max values.
*/
using TestMain.Definitions;
using System.Collections.Generic;

namespace TestMain.StackAndQueue
{
    class MaxSlidingWindow : Solution
    {
        public override void Run()
        {
            var test = new int[] { 1, 3, -1, -3, 5, 3, 6, 7 };
            var expected = new int[] { 3, 3, 5, 5, 6, 7 };
            AssertEqual(expected, MaxSlidingWindowInternal(test, 3));
        }

        private int[] MaxSlidingWindowInternal(int[] nums, int k)
        {
            var res = new int[nums.Length - k + 1];
            var deque = new LinkedList<int>();
            for (int i = 0; i < nums.Length; i++)
            {
                // The deque is monotonically decreasing per the nums[index]. Each index will be visited at most twice.
                while (deque.Count > 0 && nums[i] >= nums[deque.Last.Value])
                {
                    deque.RemoveLast();
                }
                deque.AddLast(i);
                
                // Deque has "k+1" numbers now
                if (deque.First.Value == i - k)
                {
                    deque.RemoveFirst();
                }

                // Start to fill results
                if (i >= k - 1)
                {
                    res[i - k + 1] = nums[deque.First.Value];
                }
            }

            return res;
        }
    }
}

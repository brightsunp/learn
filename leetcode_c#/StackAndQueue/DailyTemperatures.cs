/**
* Given an array of integers temperatures represents the daily temperatures, 
* return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
* 
* If there is no future day for which this is possible, keep answer[i] == 0 instead.
*/
using TestMain.Definitions;
using System.Collections.Generic;

namespace TestMain.StackAndQueue
{
    class DailyTemperatures : Solution
    {
        public override void Run()
        {
            var test1 = new int[] { 73, 74, 75, 71, 69, 72, 76, 73 };
            var res1 = new int[] { 1, 1, 4, 2, 1, 1, 0, 0 };
            AssertEqual(res1, DailyTemperaturesInternal(test1));
            AssertEqual(res1, DailyTemperaturesInternalStack(test1));

            var test2 = new int[] { 30, 40, 50, 60 };
            var res2 = new int[] { 1, 1, 1, 0 };
            AssertEqual(res2, DailyTemperaturesInternal(test2));
            AssertEqual(res2, DailyTemperaturesInternalStack(test2));
        }

        private int[] DailyTemperaturesInternal(int[] temperatures)
        {
            var res = new int[temperatures.Length];
            for (int i = 0; i < temperatures.Length; i++)
            {
                for (int j = i + 1; j < temperatures.Length; j++)
                {
                    if (temperatures[j] > temperatures[i])
                    {
                        res[i] = j - i;
                        break;
                    }
                }
            }

            return res;
        }

        // Stack to store all the unsolved indexes; later if there's a larger value, resolve them.
        // The stack is monotonically decreasing per the temperatures[index]. Each index will be visited at most twice.
        private int[] DailyTemperaturesInternalStack(int[] temperatures)
        {
            var stack = new Stack<int>();
            var res = new int[temperatures.Length];
            for (int i = 0; i < temperatures.Length; i++)
            {
                while (stack.Count > 0 && temperatures[i] > temperatures[stack.Peek()])
                {
                    int j = stack.Pop();
                    res[j] = i - j;
                }
                stack.Push(i);
            }

            return res;
        }
    }
}

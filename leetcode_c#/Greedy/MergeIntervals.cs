/**
* Given an array of intervals where intervals[i] = [start-i, end-i], 
* Merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
* 
* 1 <= intervals.length <= 10^4, intervals[i].length == 2
*/
using System;
using System.Collections.Generic;
using TestMain.Definitions;

namespace TestMain.Greedy
{
    class MergeIntervals : Solution
    {
        public override void Run()
        {
            AssertEqual(new int[][] { new int[] { 1, 7 }, new int[] { 8, 10 }, new int[] { 15, 18 } },
                Merge(new int[][] { new int[] { 8, 10 }, new int[] { 1, 3 }, new int[] { 2, 6 }, new int[] { 6, 7 }, new int[] { 15, 18 } }));
        }

        private int[][] Merge(int[][] intervals)
        {
            Array.Sort(intervals, (x, y) => x[0] - y[0]);
            var res = new List<int[]>();
            foreach (int[] interval in intervals)
            {
                int curLen = res.Count;
                if (curLen > 0 && interval[0] <= res[curLen - 1][1])
                {
                    if (interval[1] > res[curLen - 1][1])
                    {
                        res[curLen - 1][1] = interval[1];
                    }
                }
                else
                {
                    res.Add(interval);
                }
            }
            return res.ToArray();
        }
    }
}

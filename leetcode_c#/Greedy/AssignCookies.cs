/**
* Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. 
* If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content.
* 
* Your goal is to maximize the number of your content children and output the maximum number. But, you should give each child at most one cookie.
*/
using System;
using TestMain.Definitions;

namespace TestMain.Greedy
{
    class AssignCookies : Solution
    {
        public override void Run()
        {
            AssertEqual(1, FindContentChildren(new int[] { 1, 2, 3 }, new int[] { 1, 1 }));
            AssertEqual(2, FindContentChildren(new int[] { 1, 2 }, new int[] { 1, 2, 3 }));
            AssertEqual(2, FindContentChildren(new int[] { 10, 9, 8, 7 }, new int[] { 5, 6, 7, 8 }));
        }

        private int FindContentChildren(int[] g, int[] s)
        {
            Array.Sort(g);
            Array.Sort(s);
            int count = 0;
            foreach (int size in s)
            {
                if (size >= g[count])
                {
                    count++;
                }
                if (count == g.Length)
                {
                    break;
                }
            }
            return count;
        }
    }
}

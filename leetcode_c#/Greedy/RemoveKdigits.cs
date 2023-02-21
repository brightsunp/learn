/**
* Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.
* 
* 1 <= k <= num.length <= 105
* num consists of only digits. 
* num does not have any leading zeros except for the zero itself.
*/
using System.Collections.Generic;
using TestMain.Definitions;

namespace TestMain.Greedy
{
    class RemoveKdigits : Solution
    {
        public override void Run()
        {
            AssertEqual("214", RemoveKdigitsInternal("2314", 1));
            AssertEqual("14", RemoveKdigitsInternal("2314", 2));
            AssertEqual("1", RemoveKdigitsInternal("2314", 3));
            AssertEqual("0", RemoveKdigitsInternal("2314", 4));

            AssertEqual("1219", RemoveKdigitsInternal("1432219", 3));
            AssertEqual("200", RemoveKdigitsInternal("10200", 1));
            AssertEqual("0", RemoveKdigitsInternal("10", 2));
        }

        private string RemoveKdigitsInternal(string num, int k)
        {
            // Remove as many as possible BIG digits in the most significant positions on the LEFT.
            // -> Monotonically increasing stack!
            var stack = new Stack<char>();
            stack.Push(num[0]);
            for (int i = 1; i < num.Length; i++)
            {
                while (k > 0 && stack.Count > 0 && num[i] < stack.Peek())
                {
                    stack.Pop();
                    k--;
                }

                // This prevents leading zeros.
                if (stack.Count > 0 || num[i] != '0')
                {
                    stack.Push(num[i]);
                }
            }
            while (k > 0 && stack.Count > 0)
            {
                stack.Pop();
                k--;
            }

            string res = string.Empty;
            while (stack.Count > 0)
            {
                res = stack.Pop() + res;
            }
            return res == string.Empty ? "0" : res;
        }
    }
}

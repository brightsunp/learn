/**
* Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
* 
* s consists of digits, '+', '-', '(', ')', and ' '.
* s represents a valid expression.
* '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
* '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
*/
using TestMain.Definitions;
using System.Collections.Generic;

namespace TestMain.StackAndQueue
{
    class BasicCalculator : Solution
    {
        public override void Run()
        {
            AssertEqual("2", Calculate("1 + 1").ToString());
            AssertEqual("3", Calculate(" 2-1 + 2 ").ToString());
            AssertEqual("23", Calculate("(1+(4+5+2)-3)+(6+8)").ToString());
        }

        // '(': Push the previous res and isAdd into stack, reset them, then calculate new res within the parenthesis.
        // ')': Pop out top two numbers from stack, first is isAdd and second is res before this pair of parenthesis.
        private int Calculate(string s)
        {
            int res = 0, num = 0, isAdd = 1;
            var stack = new Stack<int>();
            foreach (char c in s)
            {
                if (c >= '0' && c <= '9')
                {
                    num = 10 * num + (c - '0');
                }
                else
                {
                    res += num * isAdd;
                    num = 0;

                    if (c == '+')
                    {
                        isAdd = 1;
                    }
                    if (c == '-')
                    {
                        isAdd = -1;
                    }
                    if (c == '(')
                    {
                        stack.Push(res);
                        stack.Push(isAdd);
                        res = 0;
                        isAdd = 1;
                    }
                    if (c == ')')
                    {
                        res = res * stack.Pop() + stack.Pop();
                    }
                }
            }
            res += num * isAdd;

            return res;
        }
    }
}

/**
* Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
* 
* An input string is valid if:
* Open brackets must be closed by the same type of brackets.
* Open brackets must be closed in the correct order. ("([)]{}" is not valid)
* Every close bracket has a corresponding open bracket of the same type.
*/
using TestMain.Definitions;
using System.Collections.Generic;

namespace TestMain.StackAndQueue
{
    class ValidParentheses : Solution
    {
        public override void Run()
        {
            AssertTrue(IsValid("()"));
            AssertTrue(IsValid("()[]{}"));
            AssertTrue(!IsValid("([)]{}"));
            AssertTrue(!IsValid("(]"));

            AssertTrue(IsValidWithoutMap("()"));
            AssertTrue(IsValidWithoutMap("()[]{}"));
            AssertTrue(!IsValidWithoutMap("([)]{}"));
            AssertTrue(!IsValidWithoutMap("(]"));
        }

        private bool IsValid(string s)
        {
            var map = new Dictionary<char, char>
            {
                { ')', '(' },
                { '}', '{' },
                { ']', '[' }
            };
            var stack = new Stack<char>();
            foreach (char c in s)
            {
                if (!map.ContainsKey(c))
                {
                    stack.Push(c);
                }
                else
                {
                    if (stack.Count == 0)
                    {
                        return false;
                    }
                    char top = stack.Pop();
                    if (top != map[c])
                    {
                        return false;
                    }
                }
            }

            return stack.Count == 0;
        }

        // Genius idea
        private bool IsValidWithoutMap(string s)
        {
            var stack = new Stack<char>();
            foreach (char c in s)
            {
                if (c == '(')
                {
                    stack.Push(')');
                }
                else if (c == '{')
                {
                    stack.Push('}');
                }
                else if (c == '[')
                {
                    stack.Push(']');
                }
                else if (stack.Count == 0 || stack.Pop() != c)
                {
                    return false;
                }
            }

            return stack.Count == 0;
        }
    }
}

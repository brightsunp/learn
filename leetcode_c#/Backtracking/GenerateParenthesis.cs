/**
* Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses. 
* (1 <= n <= 8)
* 
* Input: n = 3
* Output: ["((()))","(()())","(())()","()(())","()()()"]
*/
using System.Collections.Generic;
using TestMain.Definitions;

namespace TestMain.Backtracking
{
    class GenerateParenthesis : Solution
    {
        public override void Run()
        {
            TestOutput(nameof(GenerateParenthesisInternal), $"[{string.Join(", ", GenerateParenthesisInternal(3))}]");
        }

        private IList<string> GenerateParenthesisInternal(int n)
        {
            var solutions = new List<string>();
            ParenthesisInternal(n, n, "", solutions);
            return solutions;
        }

        // The more parameters, the clearer code logic.
        private void ParenthesisInternal(int left, int right, string solution, IList<string> solutions)
        {
            if (left > right)
            {
                return;
            }
            else if (left == 0 && right == 0)
            {
                solutions.Add(solution);
            }
            else
            {
                if (left > 0)
                {
                    ParenthesisInternal(left - 1, right, solution + '(', solutions);
                }
                if (right > 0)
                {
                    ParenthesisInternal(left, right - 1, solution + ')', solutions);
                }
            }
        }
    }
}

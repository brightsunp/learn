/**
* 1. Decision Problem - find a feasible solution.
* 2. Optimization Problem - find the best solution.
* 3. Enumeration Problem - find all feasible solutions.
*/
using System.Collections.Generic;
using System.Linq;
using TestMain.Definitions;

namespace TestMain.Backtracking
{
    class RecursiveBacktracking : Solution
    {
        public override void Run()
        {
            TestOutput(nameof(Subsets), WrapListToString(Subsets(new int[] { 1, 2, 3 })));
        }

        private string WrapListToString(IList<IList<int>> lists)
        {
            IEnumerable<string> stringList = lists.Select(l => $"[{string.Join(",", l)}]");
            return $"[{string.Join(",", stringList)}]";
        }

        private IList<IList<int>> Subsets(int[] nums)
        {
            var solutions = new List<IList<int>>();
            SubsetsInternal(nums, 0, new List<int>(), solutions);
            return solutions;
        }

        private void SubsetsInternal(int[] nums, int pos, IList<int> solution, IList<IList<int>> solutions)
        {
            solutions.Add(new List<int>(solution));
            for (int i = pos; i < nums.Length; i++)
            {
                solution.Add(nums[i]);
                SubsetsInternal(nums, i + 1, solution, solutions);
                solution.RemoveAt(solution.Count - 1);
            }
        }
    }
}

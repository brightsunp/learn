/**
* 1. Decision Problem - find a feasible solution.
* 2. Optimization Problem - find the best solution.
* 3. Enumeration Problem - find all feasible solutions.
* 
* Figure out what to do in the loop, and when to turn back for a recursive method call.
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
            TestOutput(nameof(PalindromePartition), WrapStringListToString(PalindromePartition("aaba")));
            TestOutput(nameof(CombinationSum), WrapIntListToString(CombinationSum(new int[] { 10, 1, 2, 7, 6, 1, 5 }, 8)));
            TestOutput(nameof(Combinations), WrapIntListToString(Combinations(4, 2)));
            TestOutput(nameof(Permutations), WrapIntListToString(Permutations(new int[] { 1, 2, 3 })));
            TestOutput(nameof(Subsets), WrapIntListToString(Subsets(new int[] { 1, 2, 3 })));
        }

        private string WrapIntListToString(IList<IList<int>> lists)
        {
            IEnumerable<string> stringList = lists.Select(l => $"[{string.Join(",", l)}]");
            return $"[{string.Join(", ", stringList)}]";
        }

        private string WrapStringListToString(IList<IList<string>> lists)
        {
            IEnumerable<string> stringList = lists.Select(l => $"[{string.Join(",", l)}]");
            return $"[{string.Join(", ", stringList)}]";
        }

        // This is a generic solution to the recursive backtracking problems.
        private IList<IList<int>> Subsets(int[] nums)
        {
            var solutions = new List<IList<int>>();
            SubsetsInternal(nums, 0, new List<int>(), solutions);
            return solutions;
        }

        private void SubsetsInternal(int[] nums, int start, IList<int> solution, IList<IList<int>> solutions)
        {
            // Create and insert a deep copy of the solution.
            solutions.Add(new List<int>(solution));
            // Key point of the loop: we have exactly (n, n-1, n-2, ...) choices when adding the (1st, 2nd, 3rd, ...) number to the solution.
            for (int i = start; i < nums.Length; i++)
            {
                solution.Add(nums[i]);
                SubsetsInternal(nums, i + 1, solution, solutions);
                // Pop out the added num1, then push in num2 and do backtrack again.
                solution.RemoveAt(solution.Count - 1);
            }
        }

        private IList<IList<int>> Permutations(int[] nums)
        {
            var solutions = new List<IList<int>>();
            PermuteInternal(nums, new List<int>(), solutions);
            return solutions;
        }

        private void PermuteInternal(int[] nums, IList<int> solution, IList<IList<int>> solutions)
        {
            if (solution.Count == nums.Length)
            {
                solutions.Add(new List<int>(solution));
            }
            else
            {
                for (int i = 0; i < nums.Length; i++)
                {
                    // Skip duplicate number
                    if (solution.Contains(nums[i])) continue;

                    solution.Add(nums[i]);
                    PermuteInternal(nums, solution, solutions);
                    solution.RemoveAt(solution.Count - 1);
                }
            }
        }

        // Since combinations are unordered, this problem is more like Subsets.
        private IList<IList<int>> Combinations(int n, int k)
        {
            var solutions = new List<IList<int>>();
            CombineInternal(n, k, 1, new List<int>(), solutions);
            return solutions;
        }

        private void CombineInternal(int n, int k, int start, IList<int> solution, IList<IList<int>> solutions)
        {
            if (solution.Count == k)
            {
                solutions.Add(new List<int>(solution));
            }
            else
            {
                for (int i = start; i <= n; i++)
                {
                    solution.Add(i);
                    CombineInternal(n, k, i + 1, solution, solutions);
                    solution.RemoveAt(solution.Count - 1);
                }
            }
        }

        // Speed up the process to reach ending condition.
        private IList<IList<int>> CombinationSum(int[] candidates, int target)
        {
            var solutions = new List<IList<int>>();
            System.Array.Sort(candidates);
            CombinationSumInternal(candidates, target, 0, new List<int>(), solutions);
            return solutions;
        }

        private void CombinationSumInternal(int[] nums, int remain, int start, IList<int> solution, IList<IList<int>> solutions)
        {
            if (remain < 0) return;
            
            if (remain == 0)
            {
                solutions.Add(new List<int>(solution));
            }
            else
            {
                for (int i = start; i < nums.Length; i++)
                {
                    // Skip duplicate combinations
                    if (i > start && nums[i] == nums[i - 1]) continue;

                    solution.Add(nums[i]);
                    CombinationSumInternal(nums, remain - nums[i], i + 1, solution, solutions);
                    solution.RemoveAt(solution.Count - 1);
                }
            }
        }

        // Figure out when to add a palindrome string, and when to terminate the backtracking.
        private IList<IList<string>> PalindromePartition(string s)
        {
            var solutions = new List<IList<string>>();
            PartitionInternal(s, 0, new List<string>(), solutions);
            return solutions;
        }

        private void PartitionInternal(string s, int start, IList<string> solution, IList<IList<string>> solutions)
        {
            if (start == s.Length)
            {
                solutions.Add(new List<string>(solution));
            }
            else
            {
                for (int i = start; i < s.Length; i++)
                {
                    if (IsPalindrome(s, start, i))
                    {
                        solution.Add(s.Substring(start, i - start + 1));
                        PartitionInternal(s, i + 1, solution, solutions);
                        solution.RemoveAt(solution.Count - 1);
                    }
                }
            }
        }

        private bool IsPalindrome(string s, int lo, int hi)
        {
            while (lo < hi)
            {
                if (s[lo++] != s[hi--]) return false;
            }
            return true;
        }
    }
}

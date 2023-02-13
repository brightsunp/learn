/**
* Given a string s, find the longest palindromic subsequence's length in s.
* A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
*/
using TestMain.Definitions;

namespace TestMain.DynamicProgramming
{
    class LongestPalindromeSubsequence : Solution
    {
        public override void Run()
        {
            AssertEqual(4, LengthOfLps("bbbab"));
            AssertEqual(2, LengthOfLps("cbbd"));

            AssertEqual("bbb", ContinuousLps("bbbab"));
            AssertEqual("bb", ContinuousLps("cbbd"));
        }

        // Define sub problem: dp[i, j] is the length of LPS for substring(i, j), such that dp[0, s.Length-1] is the answer.
        // Can be optimized as O(n) space as well.
        private int LengthOfLps(string s)
        {
            int[,] dp = new int[s.Length, s.Length];
            for (int i = s.Length - 1; i >= 0; i--)
            {
                dp[i, i] = 1;
                for (int j = i + 1; j < s.Length; j++)
                {
                    if (s[i] == s[j])
                    {
                        dp[i, j] = dp[i + 1, j - 1] + 2;
                    }
                    else
                    {
                        dp[i, j] = System.Math.Max(dp[i + 1, j], dp[i, j - 1]);
                    }
                }
            }

            return dp[0, s.Length - 1];
        }

        // Two pointers: leverage the characteristics of palindrome string, and avoid duplicate searches.
        // O(n*n) time and O(1) space
        private string ContinuousLps(string s)
        {
            int res_start = 0, res_len = 1;
            for (int i = 0; i < s.Length; i++)
            {
                int right = i + 1;
                while (right < s.Length && s[right] == s[i])
                {
                    right++;
                }
                // s[i, right - 1] inclusive is palindrome.

                int left = i - 1;
                while (left >= 0 && right < s.Length && s[left] == s[right])
                {
                    left--;
                    right++;
                }
                // s[left + 1, right - 1] inclusive is palindrome.

                int cur_len = right - left - 1;
                if (cur_len > res_len)
                {
                    res_len = cur_len;
                    res_start = left + 1;
                }
            }
            return s.Substring(res_start, res_len);
        }
    }
}

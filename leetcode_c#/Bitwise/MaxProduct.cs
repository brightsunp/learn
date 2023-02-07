/**
* Given a string array words, return the maximum value of length(words[i]) * length(words[j]) where the two words do not share common letters. 
* If no such two words exist, return 0.
* 
* 1) 2 <= words.length <= 1000
* 2) 1 <= words[i].length <= 1000
* 3) words[i] consists only of lowercase English letters.
*/
using TestMain.Definitions;

namespace TestMain.Bitwise
{
    class MaxProduct : Solution
    {
        public override void Run()
        {
            AssertEqual(16, MaxProductInternal(new string[] { "abcw", "baz", "foo", "bar", "xtfn", "abcdef" }));
            AssertEqual(4, MaxProductInternal(new string[] { "a", "ab", "abc", "d", "cd", "bcd", "abcd" }));
            AssertEqual(0, MaxProductInternal(new string[] { "a", "aa", "aaa", "aaaa" }));
        }

        private int MaxProductInternal(string[] words)
        {
            var mask = new int[words.Length];
            var res = 0;
            for (int i = 0; i < words.Length; i++)
            {
                foreach (char c in words[i])
                {
                    mask[i] |= 1 << (c - 'a');
                }
                for (int j = 0; j < i; j++)
                {
                    if ((mask[i] & mask[j]) == 0)
                    {
                        res = System.Math.Max(res, words[i].Length * words[j].Length);
                    }
                }
            }
            return res;
        }
    }
}

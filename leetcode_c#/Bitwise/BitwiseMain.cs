/**
* Bitwise operators: &, |, >>, <<, ~, ^.
* 
* 1) 1^1=0, 0^1=1; 0^0=0, 1^0=1
* 2) if n is a power of 2, then: n&(n-1)=0
* 3) n^n=0, n^0=n, n&(~0)=n, n&(~n)=0
* 4) n&~(n-1) returns binary number containing the rightmost set bit: 1100 => 100, 1101 => 1
*/
using TestMain.Definitions;

namespace TestMain.Bitwise
{
    class BitwiseMain : Solution
    {
        public override void Run()
        {
            AssertEqual(6, SetBit(4, 1));
            AssertEqual(4, UnsetBit(6, 1));
            AssertEqual(6, SwitchBit(4, 1));
            AssertEqual(4, SwitchBit(6, 1));
            AssertTrue(CheckIfBitSet(6, 1));
            AssertTrue(!CheckIfBitSet(4, 1));

            AssertEqual(1, CountBits(4));
            AssertEqual(2, CountBits(6));

            AssertEqual(new int[] { 0, 1, 1, 2, 1, 2 }, CountingBits(5));
            AssertEqual(2, HammingDistance(1, 4));
            AssertEqual(1, HammingDistance(1, 3));
        }

        private int SetBit(int num, int pos)
        {
            return num | (1 << pos);
        }

        private int UnsetBit(int num, int pos)
        {
            return num & (~(1 << pos));
        }

        private int SwitchBit(int num, int pos)
        {
            return num ^ (1 << pos);
        }

        private bool CheckIfBitSet(int num, int pos)
        {
            // or ((num >> pos) & 1) > 0
            return (num & (1 << pos)) > 0;
        }

        private int CountBits(int num)
        {
            int count = 0;
            while (num > 0)
            {
                count += num & 1;
                num >>= 1;
            }
            return count;
        }

        private int[] CountingBits(int n)
        {
            var res = new int[n + 1];
            for (int i = 0; i <= n; i++)
            {
                res[i] = res[i >> 1] + (i & 1);
            }
            return res;
        }

        private int HammingDistance(int x, int y)
        {
            return CountBits(x ^ y);
        }
    }
}

/**
* Bitwise operators: &, |, >>, <<, ~, ^.
* 
* 1) 1^1=0, 0^1=1; 0^0=0, 1^0=1
* 2) if n is a power of 2, then: n&(n-1)=0
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
                count += (num & 1);
                num >>= 1;
            }
            return count;
        }
    }
}

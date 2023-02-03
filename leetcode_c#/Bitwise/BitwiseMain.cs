/**
* Bitwise operators: &, |, >>, <<, ~, ^.
* 
* 1) 1^1=0, 0^1=1; 0^0=0, 1^0=1
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
            return (num & (1 << pos)) > 0;
        }
    }
}

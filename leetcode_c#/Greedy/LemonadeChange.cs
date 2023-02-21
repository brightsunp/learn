/**
* At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). 
* Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. 
* You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
* 
* Note that you do not have any change in hand at first.
*/
using TestMain.Definitions;

namespace TestMain.Greedy
{
    class LemonadeChange : Solution
    {
        public override void Run()
        {
            AssertTrue(LemonadeChangeInternal(new int[] { 5, 5, 5, 10, 20 }));
            AssertTrue(!LemonadeChangeInternal(new int[] { 5, 5, 10, 10, 20 }));
        }

        private bool LemonadeChangeInternal(int[] bills)
        {
            int fives = 0, tens = 0;
            foreach (int bill in bills)
            {
                switch (bill)
                {
                    case 5:
                        fives++;
                        continue;

                    case 10:
                        fives--;
                        tens++;
                        break;

                    case 20:
                        fives--;
                        if (tens > 0)
                        {
                            tens--;
                        }
                        else
                        {
                            fives -= 2;
                        }
                        break;
                }
                if (fives < 0)
                {
                    return false;
                }
            }
            return true;
        }
    }
}

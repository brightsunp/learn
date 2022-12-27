/**
* Definition for solution.
*/
using System;

namespace TestMain.Definitions
{
    abstract class Solution
    {
        public abstract void Run();

        public virtual void TestOutput(string methodName, object output)
        {
            Console.WriteLine($"Test Output of {GetType().Name} solution - {methodName} method: \n{output}");
            Console.ReadKey();
        }
    }
}

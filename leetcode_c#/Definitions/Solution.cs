/**
* Definition for solution.
*/
using System;

namespace TestMain.Definitions
{
    abstract class Solution
    {
        public abstract void Run();

        public virtual void TestOutput(string methodName, string output)
        {
            Console.WriteLine($"Test Output of {this.GetType().Name} solution - {methodName} method: \n{output}");
            Console.ReadKey();
        }
    }
}

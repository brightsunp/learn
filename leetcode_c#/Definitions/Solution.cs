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
            WriteInformation($"Test Output of {GetType().Name} solution - {methodName} method: \n{output}\n");
        }

        public virtual void AssertNull(object output)
        {
            if (output != null)
            {
                WriteError($"Test failed! Output is not null: {output}");
            }
        }

        public virtual void AssertEqual(string expected, string actual)
        {
            if (expected != actual)
            {
                WriteError($"Test failed! Expected is {expected}, but actual is {actual}");
            }
        }

        protected void WriteInformation(string message)
        {
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine(message);
            Console.ResetColor();
            Console.ReadKey();
        }

        protected void WriteError(string errorMessage)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine(errorMessage);
            Console.ResetColor();
            Console.ReadKey();
        }
    }
}

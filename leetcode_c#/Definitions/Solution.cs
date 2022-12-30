/**
* Definition for solution.
*/
using System;
using System.Runtime.CompilerServices;

namespace TestMain.Definitions
{
    public abstract class Solution
    {
        public abstract void Run();

        public virtual void TestOutput(string methodName, object output)
        {
            WriteInformation($"Test Output from {GetType().Name} solution - {methodName} method: \n{output}\n");
        }

        public virtual void AssertNull(object output, [CallerLineNumber]int line = 0)
        {
            if (output != null)
            {
                WriteError($"Test failed from {GetType().Name} solution at line {line}: \nOutput is not null: {output}");
            }
        }

        public virtual void AssertTrue(bool output, [CallerLineNumber] int line = 0)
        {
            if (!output)
            {
                WriteError($"Test failed from {GetType().Name} solution at line {line}: \nOutput is false");
            }
        }

        public virtual void AssertEqual(object expected, object actual, [CallerLineNumber] int line = 0)
        {
            if (expected.ToString() != actual.ToString())
            {
                WriteError($"Test failed from {GetType().Name} solution at line {line}: \nExpected is {expected}, but actual is {actual}");
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

/**
* Definition for solution.
*/
using System;
using System.Collections;
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
            if (expected is IEnumerable && actual is IEnumerable)
            {
                bool isEqual = true;
                var expIter = (expected as IEnumerable).GetEnumerator();
                var actIter = (actual as IEnumerable).GetEnumerator();
                while (expIter.MoveNext() && actIter.MoveNext())
                {
                    if (expIter.Current is IEnumerable && actIter.Current is IEnumerable)
                    {
                        AssertEqual(expIter.Current, actIter.Current);
                    }

                    if (expIter.Current.ToString() != actIter.Current.ToString())
                    {
                        isEqual = false;
                        break;
                    }
                }
                if (expIter.MoveNext() || actIter.MoveNext())
                {
                    isEqual = false;
                }

                if (!isEqual)
                {
                    WriteError($"Test failed from {GetType().Name} solution at line {line}: \nExpected and actual arrays are not the same");
                }
            }
            else if (expected.ToString() != actual.ToString())
            {
                WriteError($"Test failed from {GetType().Name} solution at line {line}: \nExpected is {expected}, but actual is {actual}");
            }
        }

        private void WriteInformation(string message)
        {
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine(message);
            Console.ResetColor();
            Console.ReadKey();
        }

        private void WriteError(string errorMessage)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine(errorMessage);
            Console.ResetColor();
            Console.ReadKey();
        }
    }
}

/**
* Given two integer arrays pushed and popped each with distinct values, 
* return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.
* 
* All the elements of pushed are unique, and popped is a permutation of pushed.
*/
using TestMain.Definitions;
using System.Collections.Generic;

namespace TestMain.StackAndQueue
{
    class StackSequences : Solution
    {
        public override void Run()
        {
            var pushed1 = new int[] { 1, 2, 3, 4, 5 };
            var popped1 = new int[] { 4, 5, 3, 2, 1 };
            AssertTrue(ValidateStackSequences(pushed1, popped1));

            var pushed2 = new int[] { 1, 2, 3, 4, 5 };
            var popped2 = new int[] { 4, 5, 3, 1, 2 };
            AssertTrue(!ValidateStackSequences(pushed2, popped2));
        }

        private bool ValidateStackSequences(int[] pushed, int[] popped)
        {
            var stack = new Stack<int>();
            int index = 0;
            foreach (int val in pushed)
            {
                stack.Push(val);
                while (stack.Count > 0 && stack.Peek() == popped[index])
                {
                    stack.Pop();
                    index++;
                }
            }

            return stack.Count == 0;
        }
    }
}

/**
* Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
* 
* Implement all the functions:
* 1. void push(int x) Pushes element x to the back of the queue.
* 2. int pop() Removes the element from the front of the queue and returns it.
* 3. int peek() Returns the element at the front of the queue.
* 4. boolean empty() Returns true if the queue is empty, false otherwise.
* 
* All the calls to pop and peek are valid. You must use only standard operations of a stack (push, peek, pop, and empty).
*/
using System.Collections.Generic;
using TestMain.Definitions;

namespace TestMain.StackAndQueue
{
    class MyQueue : Solution
    {
        private Stack<int> inputs = new Stack<int>();
        private Stack<int> outputs = new Stack<int>();

        public override void Run()
        {
            MyQueue myQueue = new MyQueue();
            
            myQueue.Push(1);
            myQueue.Push(2);
            AssertEqual(1, myQueue.Peek());
            myQueue.Pop();
            AssertEqual(2, myQueue.Peek());
            AssertTrue(!myQueue.Empty());
            myQueue.Pop();
            AssertTrue(myQueue.Empty());
        }

        public void Push(int x)
        {
            inputs.Push(x);
        }

        public int Pop()
        {
            _ = Peek();
            return outputs.Pop();
        }

        // Amortized O(1) time complexity. In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.
        public int Peek()
        {
            if (outputs.Count == 0)
            {
                while (inputs.Count != 0)
                {
                    outputs.Push(inputs.Pop());
                }
            }

            return outputs.Peek();
        }

        public bool Empty()
        {
            return inputs.Count == 0 && outputs.Count == 0;
        }
    }
}

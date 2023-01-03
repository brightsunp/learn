/**
* Entry to test all the sorting snippets.
*/
using TestMain.Definitions;
using TestMain.Snippets;

namespace TestMain.Sort
{
    class SortMain : Solution
    {
        public override void Run()
        {
            var expected = Array.SampleExpected();
            var actual = Array.SampleActual();
            actual.BubbleSort();
            AssertEqual(expected, actual);

            actual = Array.SampleActual();
            actual.SelectionSort();
            AssertEqual(expected, actual);

            actual = Array.SampleActual();
            actual.InsertionSort();
            AssertEqual(expected, actual);

            actual = Array.SampleActual();
            actual.MergeSort();
            AssertEqual(expected, actual);

            for (int i = 0; i < 10; i++)
            {
                actual = Array.SampleActual();
                actual.QuickSort();
                AssertEqual(expected, actual);
            }

            actual = Array.SampleActual();
            actual.CountingSort();
            AssertEqual(expected, actual);
        }
    }
}

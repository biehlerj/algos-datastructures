package binary_search

import "testing"

type binarySearchTest struct {
        arr []int64
        arrLen, target, expected int64
}

var arr = []int64{2, 3, 4, 10, 40}
var arrLen = int64(len(arr) - 1)

var binarySearchTests = []binarySearchTest{
        {arr, arrLen, 10, 3},
        {arr, arrLen, 13, -1},
}

func TestBinarySearch(t *testing.T) {
        for _, test := range binarySearchTests {
                if output := BinarySearch(test.arr, test.arrLen, test.target); output != test.expected {
                        t.Errorf("Output %q not equal to expected %q", output, test.expected)
                }
        }
}

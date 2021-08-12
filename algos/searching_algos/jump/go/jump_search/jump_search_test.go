package jump_search

import "testing"

type jumpSearchTest struct {
	arr                      []int64
	arrLen, target, expected int64
}

var arr = []int64{0, 0, 4, 7, 10, 23, 34, 40, 55, 68, 77, 90}
var arrLen = int64(len(arr) - 1)

var jumpSearchTests = []jumpSearchTest{
	{arr, arrLen, 10, 4},
	{arr, arrLen, 69, -1},
}

func TestBinarySearch(t *testing.T) {
	for _, test := range jumpSearchTests {
		if output := JumpSearch(test.arr, test.arrLen, test.target); output != test.expected {
			t.Errorf("Output %q not equal to expected %q", output, test.expected)
		}
	}
}

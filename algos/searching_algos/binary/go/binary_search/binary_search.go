package binary_search

import "math"

// BinarySearch searches an array of n length looking for the target
// It does so following the binary search algorithm:
// https://en.wikipedia.org/wiki/Binary_search_algorithm
// It returns the index where the target is or -1 if the target isn't present
func BinarySearch(arr []int64, arrLen int64, target int64) int64 {
        var left int64 = 0;
        right := arrLen - 1;

        for left <= right {
                leftRightMath := left + right / 2;
                floatMiddle := math.Floor(float64(leftRightMath));
                middle := int64(floatMiddle);
                
                if arr[middle] < target {
                        left = middle + 1;
                } else if arr[middle] > target {
                        right = middle - 1;
                } else {
                        return middle
                }
        }
        return -1;
}

package jump_search

import "math"

// JumpSearch searches an array of n length looking for the given target
// It does so following the jump search algorithm:
// TODO wikipedia link
// It return the index where the target is or -1 if the target isn't present
func JumpSearch(arr []int64, arrLen int64, target int64) int64 {
	var lower int64 = 0
	var jump float64 = math.Floor(math.Sqrt(float64(arrLen)))

	for arr[int64(math.Min(jump, float64(arrLen))-1)] < target {
		lower = int64(jump)
		jump += jump
		if lower >= arrLen {
			return -1
		}
	}

	for arr[lower] < target {
		lower += 1
		if float64(lower) == math.Min(jump, float64(arrLen)) {
			return -1
		}
	}

	if arr[lower] == target {
		return lower
	}
	return -1
}

/**
 * @param {Array<number>} arr - The array to search
 * @param {number}        arrLen - The length of the array to search
 * @param {number}        target - The item to find in the array
 * @return {number}       The index of the target or -1 if the target isn't present
 */
export function binarySearch(arr: Array<number>, arrLen: number, target: number): number {
    let left = 0;
    let right = arrLen - 1;

    while (left <= right) {
        const middle = Math.floor((left + right) / 2);

        if (arr[middle] < target)
            left = middle + 1;
        else if (arr[middle] > target)
            right = middle - 1;
        else return middle;
    }
    return -1;
}

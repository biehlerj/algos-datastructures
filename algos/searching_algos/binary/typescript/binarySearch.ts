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

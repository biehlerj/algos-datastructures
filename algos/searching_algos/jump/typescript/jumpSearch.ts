/**
* Implementation of the jump search algorithm
*
* @param  {Array<number>} arr    - The array to search
* @param  {number}        arrLen - The length of the array to search
* @param  {number}        target - The item to find in the array
* @return {number}        The index of the target or -1 if the target isn't present
*/
export function jumpSearch(arr: Array<number>, arrLen: number, target: number): number {
    let lower = 0;
    let jump = Math.floor(Math.sqrt(arrLen));

    while (arr[Math.min(jump, arrLen) - 1] < target) {
        lower = jump;
        jump += jump;
        // TODO: Write test case for this line
        if (lower >= arrLen)
            return -1;
    }

    while (arr[lower] < target) {
        lower += 1;
        // TODO: Write test case for this line
        if (lower === Math.min(jump, arrLen)) 
            return -1;
    }

    if (arr[lower] === target)
        return lower;
    return -1;
}

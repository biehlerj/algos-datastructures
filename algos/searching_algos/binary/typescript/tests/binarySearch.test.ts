import { binarySearch } from '../binarySearch';

describe('test binary search', function () {
    it('good array', function() {
        const arr = [2, 3, 4, 10, 40];
        const n = arr.length;
        const x = 10;
        const result = binarySearch(arr, n, x);
        expect(result).toBe(3);
    });

    it('array with missing target', function() {
        const arr = [2, 3, 5, 10, 40];
        const n = arr.length;
        const x = 14;
        const result = binarySearch(arr, n, x);
        expect(result).toBe(-1);
    });
});

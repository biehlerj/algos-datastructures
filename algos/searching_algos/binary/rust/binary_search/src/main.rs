use std::cmp::Ordering;

/// Implementation of the binary search algorithm
///
/// Arguments:
///
/// * `target` - The item to search for in the array
/// * `arr`    - The array to search
/// 
/// Returns:
///
/// * `usize`  - The numeric representation of the index where target was found
/// * `None`   - If nothing is found returns None
pub fn binary_search<T: Ord>(target: &T, arr: &[T]) -> Option<usize> {
    let mut left = 0;
    let mut right = arr.len();

    while left < right {
        let middle = left + (right - left) / 2;

        match target.cmp(&arr[middle]) {
            Ordering::Less => right = middle,
            Ordering::Equal => return Some(middle),
            Ordering::Greater => left = middle +1,
        }
    }
    None
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn empty() {
        let result = binary_search(&"a", &vec![]);
        assert_eq!(result, None);
    }

    #[test]
    fn one_item() {
        let result = binary_search(&"a", &vec!["a"]);
        assert_eq!(result, Some(0));
    }

    #[test]
    fn search_strings() {
        let result = binary_search(&"a", &vec!["a", "b", "c", "d", "google", "zoo"]);
        assert_eq!(result, Some(0));
    }

    #[test]
    fn search_ints () {
        let index = binary_search(&4, &vec![1, 2, 3, 4]);
        assert_eq!(index, Some(3));

        let index = binary_search(&3, &vec![1, 2, 3, 4]);
        assert_eq!(index, Some(2));

        let index = binary_search(&2, &vec![1, 2, 3, 4]);
        assert_eq!(index, Some(1));

        let index = binary_search(&1, &vec![1, 2, 3, 4]);
        assert_eq!(index, Some(0));
    }

    #[test]
    fn not_found() {
        let index = binary_search(&5, &vec![1, 2, 3, 4]);
        assert_eq!(index, None);
    }
}

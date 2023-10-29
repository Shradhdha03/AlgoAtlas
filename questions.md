## What algorithm does Python's `sorted()` function use and what is its time/space complexity?

The `sorted()` function in Python uses an algorithm called **Timsort**, which is a hybrid sorting algorithm derived from merge sort and insertion sort.

### Time Complexity:
- **Best Case:** \(O(n \log n)\)
- **Average Case:** \(O(n \log n)\)
- **Worst Case:** \(O(n \log n)\)

Timsort is designed to perform well on many kinds of real-world data. It takes advantage of runs of consecutive ordered elements that already exist in most real-world data, and it tries to optimize the performance across various scenarios.

### Space Complexity:
- **Worst Case:** \(O(n)\)

Timsort requires a temporary array to store the data, leading to a linear space complexity in the worst case.

> Note: While `sorted()` returns a new list with the sorted elements, the built-in method `list.sort()` sorts the list in place (modifying the original list) and has the same time and space complexity as `sorted()`.




## What is the best sorting algorithm for the problem?

## Problem

Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

### Sorting Algorithms:
1. **Quick Sort**: Average and Worst-case time complexity of \(O(n \log n)\). Might have poor performance on already sorted or nearly sorted arrays, depending on the pivot selection strategy.
2. **Merge Sort**: Time complexity is \(O(n \log n)\) in all cases. Consistent performance but requires \(O(n)\) additional space.
3. **Heap Sort**: Time complexity is \(O(n \log n)\) in all cases. In-place sorting but not stable.
4. **Tim Sort**: Hybrid derived from Merge Sort and Insertion Sort. Time complexity is \(O(n \log n)\) in all cases. Designed to perform well on real-world data with runs of ordered data. Requires \(O(n)\) space.

### Recommendation:

For this specific problem, the two-pointer technique is best. But if we were to sort the squared array, **Tim Sort** (which is the default in Python's `sorted()` function) would be a good choice due to its optimization for real-world data patterns.

## Why Heap sort is not stable?

## arbitrary-precision arithmetic?

## External Merge Sort?

## Optimizing disk I/O by efficiently managing buffer sizes and minimizing the number of read and write operations?

## parallel processing?


## why O(n) + O(n-1) which is asymptotically equivalent to O(n)

When analyzing the time complexity of an algorithm, the "big O" notation \( O(f(n)) \) is used to describe an upper bound on the growth rate of the function. The constant factors and lower order terms are typically omitted because they become increasingly irrelevant as \( n \) grows larger.

Consider the expression \( O(n) + O(n-1) \):

1. \( O(n) \) describes a function that grows linearly with \( n \). The highest order term here is \( n \).

2. \( O(n-1) \) also describes a function that grows linearly with \( n \), despite the subtraction of 1. The subtraction of a constant doesn't affect the growth rate in a significant way, so the highest order term is still \( n \).

When you add these two together, the dominant term remains \( n \). Therefore, the combined time complexity is still on the order of \( n \).

So, \( O(n) + O(n-1) \) is asymptotically equivalent to \( O(n) \).

Another way to think about it: As \( n \) gets very large, the difference between \( n \) and \( n-1 \) becomes increasingly insignificant. For example, when \( n = 1,000,000 \), \( n-1 = 999,999 \), and the difference between these two numbers is trivial in the context of big O notation. The most significant factor in determining the growth rate is the \( n \) term itself.



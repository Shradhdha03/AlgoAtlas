# Three Sum Closest

## Problem Statement

Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums` such that the sum is closest to `target`. Return the sum of the three integers. You may assume that each input would have exactly one solution.

### Constraints:

- 3 <= nums.length <= 500
- -1000 <= nums[i] <= 1000
- -10^4 <= target <= 10^4

## Test Cases

1. `nums = [-1,2,1,-4], target = 1` should return `2`
2. `nums = [0,0,0], target = 1` should return `0`
3. `nums = [1,3,-2,1,-2,3,0], target = 6` should return `6`

## Solution Explanation

The provided solution contains two methods. The first method `threeSumClosestBruteForce` is a brute force approach that generates all possible triplets and keeps track of the sum closest to the target. The second method `threeSumClosest` is an optimized solution. 

### Method 1: Brute Force

1. Initialize `closeSum` and `closeDiff` to `None`.
2. Iterate through each possible triplet combination in `nums`.
3. Calculate the `sum` and `diff` for each triplet.
4. If the `diff` is smaller than the `closeDiff`, update `closeSum` and `closeDiff`.
5. Return the `closeSum`.

```python
class Solution:

    # duplicate posible
    # indexed not matter for solution
    # there is always one answer
    # large values
    
    def threeSumClosestBruteForce(self, nums: List[int], target: int) -> int:
        closeSum = None
        closeDiff= None
        n= len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    sum= nums[i]+nums[j]+nums[k]
                    diff = abs(target -sum)
                    if closeDiff is None or diff < closeDiff:
                        closeSum = sum
                        closeDiff = abs(target-closeSum)
        return closeSum
```

### Method 2: Optimized Approach

1. Initialize `closeSum` and `closeDiff` to `None`.
2. Sort the input array `nums`.
3. Iterate through each element in `nums`.
4. Use two pointers `left` and `right` to find the triplet that gives the closest sum to `target`.
5. If the `sum` is smaller than the `target`, increment `left`, if greater, decrement `right`.
6. If the `sum` equals the `target`, return the `sum`.
7. Return the `closeSum`.

```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closeSum = None
        closeDiff= None
        n= len(nums)
        # sort
        nums.sort()
        # itereate throgh
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            # 2 pointer
            left = i+1
            right = n-1
            while left<right:
                sum = nums[i]+nums[left]+nums[right]
                diff = abs(target-sum)

                if closeDiff is None or diff < closeDiff:
                    closeSum = sum
                    closeDiff = abs(target-closeSum)

                if sum<target:
                    left+=1
                elif sum>target:
                    right-=1
                else:
                    return sum

        return closeSum
```

## Complexity Analysis

### Method 1: Brute Force

- **Time Complexity:** O(n^3), where n is the length of `nums`, as we generate all possible triplets.
- **Space Complexity:** O(1), since we use a constant amount of extra space.

### Method 2: Optimized Approach

- **Time Complexity:** O(n^2), where n is the length of `nums`. Sorting takes O(n log n) and the nested loop with two pointers takes O(n^2).
- **Space Complexity:** O(log n) to O(n), depending on the implementation of the sorting algorithm.

## Technical Follow-up Questions

1. **How would you handle very large datasets?**
   - If the input array `nums` is too large to fit into memory, how would you modify your solution?

2. **How can we further optimize the solution?**
   - Are there any heuristics or pre-processing steps that can be applied to the input array to speed up the solution?

3. **Parallelization:**
   - Can the solution be parallelized to improve performance?

4. **Memory Constraints:**
   - If the system has very limited memory, how would you modify the solution?

5. **Real-time Constraints:**
   - If the solution needs to run in real-time, for example in a streaming application, how would you modify the algorithm to handle real-time constraints?

6. **Scalability:**
   - If the constraints on the input size are relaxed, how would the solution scale, and what optimizations can be performed to handle larger inputs efficiently?

7. **Edge Cases:**
   - How does your solution handle edge cases, for example, when all elements in the array are the same or when the target is out of the range of possible sums?

8. **Alternative Approaches:**
   - Are there alternative algorithms or data structures that can solve this problem more efficiently under certain conditions?
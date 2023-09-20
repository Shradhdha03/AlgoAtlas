### Remove Element from List

[Remove Element Problem on LeetCode](https://leetcode.com/problems/remove-element/description/)

Given an integer array `nums` and an integer `val`, the challenge is to remove all occurrences of `val` in `nums` in-place. The order of the elements may be changed. The objective is to change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`. The rest of the elements in `nums` are not important. The function should return `k`.

#### Constraints to Consider:
- 0 ≤ `nums.length` ≤ 100
- 0 ≤ `nums[i]` ≤ 50
- 0 ≤ `val` ≤ 100
- in-place
- order matters
- more than 1 duplicate numbers, not in order


#### Test Cases:

```python
assert removeElement([3,2,2,3], 2) == 2
assert removeElement([0,1,2,2,3,0,4,2], 2) == 5
assert removeElement([], 2) == 0
assert removeElement([9], 9) == 0
assert removeElement([0,0,0], 0) == 0
assert removeElement([2,3,4,5,3], 1) == 5
```

#### Simple Solution:

One simple way to solve this problem is by using a new list to store elements not equal to `val` and then copying these elements back to the original list.

```python

def removeElement(nums: List[int], val: int) -> int:
    # Create a new list to store elements not equal to val.
    filtered_nums = []
    
    # Traverse the list and populate filtered_nums.
    for num in nums:
        if num != val:
            filtered_nums.append(num)

    # Replace elements in original list with elements in filtered_nums.
    for i, num in enumerate(filtered_nums):
        nums[i] = num

    # Return the length of filtered_nums.
    return len(filtered_nums)
```

##### Time and Space Complexity:

- Time Complexity: \(O(n)\), where \(n\) is the length of `nums`.
- Space Complexity: \(O(n)\), for the additional list.



#### Optimized Solution:

A more efficient approach uses the two-pointer technique. One pointer (`position`) is used to keep track of the position to place the non-val elements in the list, and the other pointer traverses the list.

```python
def removeElement(nums: List[int], val: int) -> int:
    # Initialize a pointer to track the position of non-val elements.
    position = -1
    
    # Traverse the list and update elements in-place.
    for num in nums:
        if num != val:
            position += 1
            nums[position] = num

    # Return the position + 1 which is the length of updated nums.
    return position + 1
```

##### Time and Space Complexity:

- Time Complexity: \(O(n)\), where \(n\) is the length of `nums`.
- Space Complexity: \(O(1)\), as we are not using any extra space proportional to the size of the input.

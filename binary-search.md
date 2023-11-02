## **Binary Search**

### **Problem Statement:**
Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, you are required to write a function that searches for the `target` in `nums`. If the `target` exists, the function should return its index; otherwise, it should return -1. The algorithm should have a runtime complexity of O(log n).

### **Constraints:**
- 1 ≤ `nums.length` ≤ 10^4
- -10^4 < `nums[i]`, `target` < 10^4
- All integers in `nums` are unique.
- `nums` is sorted in ascending order.

### **Test Cases:**
1. Input: `nums = [-1,0,3,5,9,12]`, `target = 9`  
   Output: `4`  
   Explanation: `9` exists in `nums` and its index is `4`.

2. Input: `nums = [-1,0,3,5,9,12]`, `target = 2`  
   Output: `-1`  
   Explanation: `2` does not exist in `nums`, so return `-1`.

### **My Solution Explanation:**
The problem is a classic example of binary search. The solution involves repeatedly dividing the search interval in half. If the value of the search key is less than the item in the middle of the interval, the algorithm narrows the interval to the lower half. Otherwise, it narrows it to the upper half. The search process repeats this process until the size of the interval is reduced to zero.

In the provided solution:
- We initialize two pointers: `start` at the beginning of the list and `end` at the end.
- The loop continues until `start` surpasses `end`.
- We calculate the middle index `mid` and check if the element at `mid` is the target.
- Depending on the comparison, we adjust our `start` or `end` pointer to continue searching in the right half of the array.
- If the target is found, its index is returned; otherwise, -1 is returned.

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize pointers for start and end of the list
        start = 0
        end = len(nums) - 1
        
        # Continue the loop as long as start does not surpass end
        while start <= end:
            # Calculate the middle index to check if the element is present at mid
            mid = start + ((end - start) // 2)

            # Check if the target value exists at the midpoint
            if nums[mid] == target:
                return mid  # Target found, return the index

            # If the target is less than the element at midpoint, 
            # move the end pointer to mid - 1
            if target < nums[mid]:
                end = mid - 1
            # Otherwise, move the start pointer to mid + 1
            else:
                start = mid + 1

        # If the loop ends, then the target element is not in the list
        return -1

```
### **Complexity Analysis:**
**Time Complexity:** O(log n)  
Because with each iteration, we are reducing the problem size by half.

**Space Complexity:** O(1)  
We are using a constant amount of space irrespective of the input size.

### **Technical Follow-up Questions:**
1. **Question:** How would you modify this binary search if the array was sorted in descending order?
   **Answer:** We would just flip the conditions. If the target is less than the element at midpoint, we would adjust the start pointer. Otherwise, we would adjust the end pointer.

2. **Question:** How would you handle duplicates in the array while ensuring O(log n) runtime complexity?
   **Answer:** Binary search inherently doesn't deal well with duplicates if we want to find the first or last occurrence. To handle this scenario while ensuring O(log n) complexity, we might need specialized variations of binary search.

3. **Question:** If given a 2D matrix where rows and columns are sorted, how would you modify this search to work?
   **Answer:** We can perform a binary search on the matrix's rows to identify the potential row where our target might reside. Once we have that, we can perform another binary search within that row. 

### **Real-world use cases:**
1. **Search Engines:** When looking up a word in a dictionary or directory.
2. **Database Systems:** To query large datasets and return results quickly.
3. **Machine Learning:** In algorithms like Decision Trees, where features are split based on certain conditions.
4. **Optimization Problems:** Where we need to find an optimal value satisfying certain conditions.
5. **Version Control Systems:** To identify changes in different versions of a document or code.

### **Powerful Questions:**
1. How can we extend this binary search approach to work on non-integer data types, such as strings or custom objects?
2. How would the algorithm change if we had multiple targets and wanted to find all their positions?
3. In what scenarios might a linear search be more practical than binary search, despite its higher time complexity?
4. Can we apply the binary search principle in domains other than searching, perhaps in optimization problems?
5. How does understanding the inner workings of binary search help when working with built-in search functions in programming libraries or databases?
```python
# The class Solution groups together two methods for the same problem.
class Solution:

    # Notes on the problem:
    # 1. We are looking for continuous subarrays.
    # 2. Duplicates are allowed.
    # 3. k can be 0, n cannot be 0, and the numbers are positive.
    # 4. Large numbers are possible in the list.

    # Testcases:
    # [10,5,2,6] 100 = 8
    # [1,2,3] 0 = 0
    # [2,5,2,3,1] 10 = 8
    # [5,4,3,2,1,0] 20 = 13
    # [2,5,2,3,1,4,7,2,1,3,4] 10 = 18

    # A brute force approach to solve the problem.
    def numSubarrayProductLessThanKBruteForce(self, nums: List[int], k: int) -> int:
        # Initialize the count to 0
        count=0
        # Get the length of the input list
        n = len(nums)
        
        # Loop through each number in the list.
        for i in range(n):
            # If the current number is less than k, increase the count.
            if nums[i] < k:
                count += 1

            # Start with a sub-product that is equal to the current number.
            sub_product = nums[i]
            j = i + 1

            # Calculate products of continuous subarrays starting at i.
            while j < n and sub_product < k:
                sub_product *= nums[j]
                if sub_product < k:
                    count += 1
                j += 1
        
        # Return the final count.
        return count

    # An optimized sliding window approach to solve the problem.
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Initialize the count and start index.
        count = 0
        start = 0

        # Get the length of the input list.
        n = len(nums)
        product = 1  # Initialize the product to 1.

        # Loop through each number in the list with 'end' as the end index of the subarray.
        for end in range(n):
            product *= nums[end]

            # If the product is greater than or equal to k, slide the window to the right.
            while product >= k and start <= end:
                product /= nums[start]
                start += 1

            # Add to the count the number of subarrays that end at the current 'end' index.
            count += end - start + 1

        # Return the final count.
        return count
```
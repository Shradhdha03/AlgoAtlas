# 3Sum Problem

## Problem Statement:

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. Notice that the solution set must not contain duplicate triplets.

### Constraints:

- `3 <= nums.length <= 3000`
- `-105 <= nums[i] <= 105`

## Test Cases:

1. `Input: nums = [-1,0,1,2,-1,-4]`
   `Output: [[-1,-1,2],[-1,0,1]]`
   
2. `Input: nums = [0,1,1]`
   `Output: []`
   
3. `Input: nums = [0,0,0]`
   `Output: [[0,0,0]]`
   
4. `Input: nums = [-1,2,-2,1,0,-1,2,-2,-3,1,0]`
   `Output: [[-3,1,2],[-2,0,2],[-2,1,1],[-1,-1,2],[-1,0,1]]`

## Solution Explanation:

The solution involves sorting the input array `nums` and then using a combination of brute force, two pointers technique, and set data structure to find all unique triplets that sum up to zero. 

1. **Brute Force Method**: The three nested loops check all possible triplets, which are then stored in a dictionary to remove duplicates.

2. **Two Pointers Technique**: For each number in the sorted array, a two-pointers technique is applied on the sub-array to its right, to find pairs whose sum with the current number is zero. 

3. **Optimized Method**: By iterating over the sorted array and applying the two-pointers technique, we directly add each found triplet as a tuple to a set, effectively removing duplicates.


```python
class Solution:
    class Solution:

    # Things to conside before writing code:
    # duplicate values possible
    # index not imortant for answer
    # large values

    def threeSumBruteForce(self, nums: List[int]) -> List[List[int]]:
        triplets = {}

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0:
                        triplet =[]
                        triplet.append(nums[i])
                        triplet.append(nums[j])
                        triplet.append(nums[k])
                        triplet.sort()
                        key=f"{triplet[0]}{triplet[1]}{triplet[2]}"
                        triplets[key]=triplet
        return list(triplets.values())

    def threeSumFirstVersion(self, nums: List[int]) -> List[List[int]]:
        triplets={}
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target= nums[i] * -1
            pairs = self.twoSum(nums, i,target)
            if len(pairs):
                for pair in pairs:
                    pair.sort()
                    key = f"{pair[0]}{pair[1]}{pair[2]}"
                    triplets[key] = pair
        return list(triplets.values())

    
    def twoSum(self, nums: List[int] ,current_pos:int,target:int)-> List[int]:
        start_index=0
        end_index=len(nums)-1
        pairs =[]

        while start_index<end_index:
            if current_pos==start_index:
                start_index+=1
            elif current_pos==end_index:
                end_index-=1
            else:
                sum=nums[start_index]+nums[end_index]
                if sum==target:
                    pairs.append([nums[start_index],nums[end_index],nums[current_pos]])
                    start_index+=1
                    end_index-=1
                elif sum>target:
                    end_index-=1
                elif sum<target:
                    start_index+=1
        return pairs


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the input list
        nums.sort()
        # Initialize the set to hold the unique triplets
        triplets = set()
        
        # Iterate through the list of numbers
        for i in range(len(nums)):
            # Avoiding duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two pointers approach to find the triplet
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    triplets.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
        
        # Convert each triplet from tuple to list
        return [list(triplet) for triplet in triplets
```

## Complexity Analysis:

### Brute Force Method:

- **Time Complexity**: $O(n^3)$, due to the three nested loops, where n is the length of the input array.
- **Space Complexity**: $O(n)$, for storing unique triplets.

### Two Pointers Technique:

- **Time Complexity**: $O(n^2)$, as for each element, we perform a linear scan of the remaining elements.
- **Space Complexity**: $O(n)$, for storing unique triplets.

### Optimized Method:

- **Time Complexity**: $O(n^2)$, similar to the Two Pointers Technique, but more efficient due to avoiding explicit checks for duplicates.
- **Space Complexity**: $O(n)$, for storing unique triplets.

## Technical Follow-up Questions:

1. **Large Datasets**: How would you optimize the solution if the input array `nums` can have up to $10^6$ elements? What kind of algorithms or data structures might be more suitable in this case?

2. **Memory Constraints**: If the system has severe memory constraints, how could the current solution be modified to reduce the space complexity? Could a trade-off between time and space complexity be beneficial here?

3. **Real-time Applications**: In real-time applications where performance is crucial, how can the current solution be improved for faster execution? Are there any algorithmic optimizations or parallel processing techniques that can be applied?

4. **Scalability**: How well does the current solution scale with increasing input size? Are there any bottlenecks in the current implementation that might limit its scalability?

5. **Data Preprocessing**: Given that `nums` is already sorted, how does this precondition affect the choice of algorithm? Would the solution be significantly different if the input array were not sorted?

6. **Distributed Computing**: If you were to solve this problem in a distributed computing environment, how would you partition the problem? What kind of challenges might arise, and how would you address them?
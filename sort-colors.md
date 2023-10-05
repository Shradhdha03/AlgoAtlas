```python
class Solution:
    def sortColorsBruteForce(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            small_num_index = i
            for j in range(i+1,n):
                if nums[j]<nums[small_num_index]:
                    small_num_index=j
            
            if i!=small_num_index:
                temp = nums[i]
                nums[i] = nums[small_num_index]
                nums[small_num_index] = temp

    def sortColors(self, nums: List[int]) -> None:
        low, mid, high =0, 0, len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[high],nums[mid]=nums[mid],nums[high]
                high-=1
```
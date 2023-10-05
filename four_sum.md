```python
class Solution:
    def fourSumBruteForce(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        quadruplets =set()
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    for m in range(k+1, n):
                        sum = int(nums[i]+nums[j]+nums[k]+nums[m])
                        if sum == target:
                            quadruplets.add((nums[i],nums[j], nums[k],nums[m]))
        return [list(quadruplet) for quadruplet in quadruplets]

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        quadruplets = []

        for i in range(n-3):
            if i>0 and nums[i-1] == nums[i]:
                continue
            in_quadruplets = self.threeSum(nums,target-nums[i],i+1)
            for in_quadruplet in in_quadruplets:
                quadruplets.append(in_quadruplet)
        return quadruplets

    def threeSum(self,nums: List[int], target:int, start_index:int):
        n = len(nums)
        quadruplets = set()
        for j in range(start_index,n):
            if j > start_index and nums[j-1] == nums[j]:
                continue
            left =j+1
            right= n-1
            while left<right:
                sum= nums[j]+nums[left]+nums[right]
                if sum ==target:
                    quadruplets.add((nums[start_index-1],nums[j],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif sum>target:
                    right-=1
                else:
                    left+=1
        return quadruplets
```
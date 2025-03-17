from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target  not in nums:
            nums.append(target)
            nums = sorted(nums)
        
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            
            
nums = [1,3,5,6]
target = 5
solution = Solution()
print(solution.searchInsert(nums, target))
from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        t = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[t] = nums[i]
                t += 1

        for i in range(t, len(nums)):
            nums[i] =0 
        return nums

nums = [1,2,2,1,1,0]
solution = Solution()
print(solution.applyOperations(nums))
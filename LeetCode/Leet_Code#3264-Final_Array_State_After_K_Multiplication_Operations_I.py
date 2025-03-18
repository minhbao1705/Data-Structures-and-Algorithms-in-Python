from typing import List

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            m = min(nums)
            for j in range(len(nums)):
                if nums[j] == m:
                    n = nums[j]*multiplier
                    nums[j] = n
                    break
        return nums
    
nums = [2,1,3,5,6]
k = 5
multiplier = 2

solution = Solution()
print(solution.getFinalState(nums, k, multiplier))
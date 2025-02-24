from typing import List

nums = [2,7,11,15]
target = 9

# Cách 1:
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         tgt = []
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []
    
# Cách 2:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i

solution = Solution()
print(solution.twoSum(nums, target))
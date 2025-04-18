from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        length = len(nums)
        res = 0
        for i in range(length - 1):
            for j in range(i + 1, length):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    res += 1
        return res

nums = [3,1,2,2,2,1,3]
k = 2

solution = Solution()
print(solution.countPairs(nums, k))
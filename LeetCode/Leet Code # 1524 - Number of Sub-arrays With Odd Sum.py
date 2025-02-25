from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        odd = 0
        even = 1
        sum = 0
        res = 0
        for i in arr:
            sum += i
            if sum % 2 == 0:
                res = (res + odd) % MOD
                even += 1
            else:
                res = (res + even) % MOD
                odd += 1
        return res
    
arr = [1, 3, 5]
solution = Solution().numOfSubarrays(arr)
print(solution)
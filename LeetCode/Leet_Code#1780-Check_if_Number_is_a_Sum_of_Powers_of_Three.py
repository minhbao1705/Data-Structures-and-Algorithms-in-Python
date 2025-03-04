from typing import List

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            remainder = n % 3
            while remainder == 2:
                return False
            n //= 3
        return True
        
n = 91
solution = Solution()
print(solution.checkPowersOfThree(n))

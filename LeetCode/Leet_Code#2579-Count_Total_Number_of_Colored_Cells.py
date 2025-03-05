from typing import List

class Solution:
    def coloredCells(self, n: int) -> int:
        return 2*(n-1)*n+1
    
n = 3
solution = Solution()
print(solution.coloredCells(n))
from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        size = n * n
        Count = [0] * (size+1)
        for i in range(n):
            for j in range(n):
                Count[grid[i][j]] += 1
                
        a, b = -1, -1
        for i in range(1, size+1):
            if Count[i] == 2:
                a = i
            elif Count[i] == 0:
                b = i

        return [a, b]
    
grid = [[9,1,7],[8,9,2],[3,4,6]]
solution = Solution()
print(solution.findMissingAndRepeatedValues(grid))
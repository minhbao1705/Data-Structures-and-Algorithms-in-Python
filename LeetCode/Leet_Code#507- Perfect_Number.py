from typing import List

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        n = int(num**0.5)
        sum = 1
        for i in range(2, n+1):
            if num % i == 0:
                sum += i + num//i
        return num==sum

num = 28
solution = Solution()
print(solution.checkPerfectNumber(num))
from typing import List

x = 121

# Cách 1:
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False

#         reverse = 0
#         xcopy = x

#         while x > 0:
#             reverse = (reverse * 10) + (x % 10)
#             x //= 10
        
#         return reverse == xcopy

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
    
solution = Solution()
print(solution.isPalindrome(x))
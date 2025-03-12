# from typing import List

# class Solution:
#     def checkPerfectNumber(self, num: int) -> bool:
#         n = num/2
#         sum = 0
#         for i in range(1, n+1):
#             if num % i == 0:
#                 sum += i
        
#         if sum == num:
#             return True
#         return False
    
num = 28
n = int(num / 2)
for i in range(1, n+1):
    print(i)

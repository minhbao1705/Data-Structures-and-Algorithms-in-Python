from typing import List

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         a = 0
#         t = -1
#         for i in haystack:
#             for j in haystack[a:len(needle)+a]:
#                 if needle==haystack[a:len(needle)+a]:
#                         t=a
#                         return t
#             a+=1
#         return t

# Cách 2:
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
            for i in range(len(haystack) - len(needle) + 1):
                if haystack[i:i+len(needle)] == needle:
                    return i
            return -1
    
haystack = "hello"
needle = "ll"

solution = Solution()
print(solution.strStr(haystack, needle))
from typing import List

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowel = ['a', 'i', 'u', 'e', 'o']
        out = 0
        for i in words[left:right+1]:
            if (i[0] in vowel) and (i[-1] in vowel):
                out += 1
        return out
    

words = ["are","amy","u"]
left = 0
right = 2
solution = Solution()
print(solution.vowelStrings(words, left, right))
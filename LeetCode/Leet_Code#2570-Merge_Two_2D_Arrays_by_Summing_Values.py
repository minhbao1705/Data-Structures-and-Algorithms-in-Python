from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        result = []

        while i<len(nums1) and j<len(nums2):
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]
            if id1 < id2:
                result.append([id1, val1])
                i += 1   
            if id2 < id1:
                result.append([id2, val2])
                j += 1
            if id1==id2:
                result.append([id2, val1 + val2])
                i += 1
                j += 1
        while i<len(nums1):
            result.append(nums1[i])
            i += 1
        while j<len(nums2):
            result.append(nums2[j])
            j += 1
        return result
    
nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]

solution = Solution()
print(solution.mergeArrays(nums1, nums2))
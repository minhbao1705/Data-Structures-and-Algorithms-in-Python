nums = [2,1,3,5,6]
k = 5
multiplier = 2


for i in range(k):
    m = min(nums)
    for j in range(len(nums)):
        if nums[j] == m:
            n = nums[j]*multiplier
            nums[j] = n
            print(nums)
            break
            
# print(nums)
nums = [1,3,5,6]
target = 2
if target  not in nums:
    nums.append(target)
    nums = sorted(nums)
    
for i in range(len(nums)):
    if nums[i] == target:
        print(i)
def moveZeroes(nums):
    left = 0
    right = 0

    # Move all non-zero elements to the beginning
    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1

    # Set all elements from left to the end as zero
    while left < len(nums):
        nums[left] = 0
        left += 1
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]

nums = [0]
moveZeroes(nums)
print(nums)  # Output: [0]

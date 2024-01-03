nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_global = nums [0]
max_current = nums[0]

for i in nums[1:]:
    max_current = max (i,max_current+ i)
    if max_current > max_global:
        max_global = max_current


print(max_global)

# Path: maximum_subarray.py
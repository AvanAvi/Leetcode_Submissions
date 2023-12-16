def trap(height):
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    trapped_water = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            trapped_water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            trapped_water += right_max - height[right]

    return trapped_water

# Test the function with the provided examples
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Expected output: 6
print(trap([4,2,0,3,2,5]))               # Expected output: 9

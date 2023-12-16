def maxArea(height):
    left=0
    right = len(height)-1

    max_area = 0

    while left < right :
        width = right-left
        currentHeight = min(height[left],height[right])
        currentArea = width * currentHeight
        max_area = max(max_area,currentArea)
    
        if height[left]< height[right]:
        
            left = left+1
        else:
            right = right-1
    return max_area

print(maxArea([1,8,6,2,5,4,8,3,7]))    
def productExceptSelf(nums):
    length = len(nums)
    answer = [0] * length
    
    # answer[i] contains the product of all the elements to the left of i
    answer[0] = 1
    for i in range(1, length):
        answer[i] = nums[i - 1] * answer[i - 1]
    
    # R contains the product of all the elements to the right of i
    R = 1
    for i in reversed(range(length)):
        # For the index 'i', R would contain the 
        # product of all elements to the right. We update R accordingly
        answer[i] = answer[i] * R
        R *= nums[i]

    return answer

# Test the function
input_array = [2, 4, 5, 1, 6]
output_array = productExceptSelf(input_array)
print(output_array)

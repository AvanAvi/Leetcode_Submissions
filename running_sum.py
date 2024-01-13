def Run_sum(nums):
    running_sum=[]
    sum=0

    for i in nums :
        sum = sum+i
        running_sum.append(sum)
    return running_sum

# Test the function
input_array = [2, 4, 5, 1, 6]  
output_array = Run_sum(input_array)
print(output_array)

def find_missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    missing_number = expected_sum - actual_sum
    return missing_number

arr = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10]
result = find_missing_number(arr)
print(f"The missing number is: {result}")

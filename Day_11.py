def insertionSort(arr):
	n = len(arr) 
	
	if n <= 1:
		return 

	for i in range(1, n):
		key = arr[i] 
		j = i-1
		while j >= 0 and key < arr[j]: 
			arr[j+1] = arr[j] 
			j -= 1
		arr[j+1] = key 
		
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

arr = [6,4,2,5]

# for insertion sort
insertionSort(arr)
print("Sorted array:")
for i in arr:
	print(i,end=" ")
      
# for binary search
K = 6
result = binary_search(arr, K)
 
if result != -1:
    print("\nElement is present at index", str(result))
else:
    print("\nElement is not present in array")
	



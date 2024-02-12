def linearSearch(L,value):
    for i in range(len(L)):
        if L[i] == value:
            return i
    return -1

arr = [2,4,6,4]
K = 6
result = linearSearch(arr,K)
if result != -1:
    print(K," is present at index ",result)
else:
    print("Element is not present")
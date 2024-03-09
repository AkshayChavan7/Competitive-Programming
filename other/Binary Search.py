def binarySearch(arr, key):
    low, high = 0, len(arr)-1 
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==key:
            return mid
        if arr[mid]<key:
            low = mid+1
        else:
            high = mid - 1
    return -1
        

arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(binarySearch(arr, 100))
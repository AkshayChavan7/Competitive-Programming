def binarySearch(arr, key, low, high):
    mid = (low+high)//2
    if low>high: return -1
    if arr[mid]==key:
        return mid
    elif arr[mid]<key:
        return binarySearch(arr, key, mid+1, high)
    else:
        return binarySearch(arr, key, low, mid-1)


arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(binarySearch(arr, 110, 0, len(arr)-1))

# Time Complexity: O(logn)
# Auxiliary Space Complexity: O(logn)
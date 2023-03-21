def binarySearch(myList: list, target, low: int, high: int):
    while low < high:
        mid = (low+high)//2
        if target > myList[mid]:
            low = mid+1
        elif target < myList[mid]:
            high = mid
        else:
            return mid
    return False
def binary_search(array, index_first, index_last, target):
    if index_first <= index_last:
        middle = (index_first + index_last) // 2
    
        if array[middle] == target:
            return True
        elif array[middle] > target:
            return binary_search(array, index_first, middle - 1, target)
        else:
            return binary_search(array, middle + 1, index_last, target)
            
    return False
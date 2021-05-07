def merge_sort(array):
    """
    Merge sort implementation.
    Sorts a list of strings, integers or floats
    """
    if len(array) > 1:
        #diving process
        middle = len(array) // 2
        half1 = merge_sort(array[:middle])
        half2 = merge_sort(array[middle:])
        #merging process
        i, j, k = 0, 0, 0
        #this will iterate until half1 or half2 runs out of elements
        while i < len(half1) and j < len(half2):
            if half1[i] <= half2[j]:
                array[k] = half1[i]
                i += 1
            else:
                array[k] = half2[j]
                j += 1
            k += 1
        #one of these will override the rest of elements
        while i < len(half1):
            array[k] = half1[i]
            k += 1
            i += 1
        while j < len(half2):
            array[k] = half2[j]
            k += 1
            j += 1  
    return array
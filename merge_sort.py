def merge(array, index_first, middle, index_last):
    #creating virtual arrays
    virtual_size1 = middle - index_first + 1
    virtual_size2 = index_last - middle
    virtual_array1 = [0] * virtual_size1
    virtual_array2 = [0] * virtual_size2
    #filling virtual arrays
    for i in range(virtual_size1):
        virtual_array1[i] = array[index_first + i]
    for j in range(virtual_size2):
        virtual_array2[j] = array[middle + 1 + j]
    #comparing and setting
    virtual_index1 = 0
    virtual_index2 = 0
    real_index = index_first
    while (virtual_index1 < virtual_size1) and (virtual_index2 < virtual_size2):
        if virtual_array1[virtual_index1] <= virtual_array2[virtual_index2]:
            array[real_index] = virtual_array1[virtual_index1]
            virtual_index1 +=1
        else:
            array[real_index] = virtual_array2[virtual_index2]
            virtual_index2 +=1
        real_index += 1
    #if there are remain elements
    while virtual_index1 < virtual_size1:
        array[real_index] = virtual_array1[virtual_index1]
        virtual_index1 += 1
        real_index += 1
    while virtual_index2 < virtual_size2:
        array[real_index] = virtual_array2[virtual_index2]
        virtual_index2 += 1
        real_index += 1



def merge_sort(array, index_first, index_last):
    if index_first < index_last:
        middle = (index_first + index_last) // 2
        merge_sort(array, index_first, middle)
        merge_sort(array, middle + 1, index_last)
        merge(array, index_first, middle, index_last)
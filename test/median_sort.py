def median_sort(array: list[int], array2: list[int]) -> float:
    '''Onlog(n)'''
    array.sort()
    array2.sort()
    return (array[len(array)//2] + array2[len(array2)//2])/2

print(median_sort([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
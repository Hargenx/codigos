'''target = 9
    array = [11, 15, 7, 9]'''

def two_sum_dumb(array: list, target: int) -> int:
    '''On²'''
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target:
                return array[i] + array[j]
    return -1

def two_sum_sort(array: list, target: int) -> int:
    '''Onlog(n)'''
    array.sort()
    for i in range(len(array)):
        if array[i] + array[i + 1] == target:
            return array[i] + array[i + 1]
    return -1

def two_sum_hash(array: list, target: int) -> int:
    hash = {}
    for idx, i in enumerate(array):
        if hash.get(i) is not None:
            return hash.get(i) + idx
        hash[target-i] = idx
    return -1

print(two_sum_dumb([11, 15, 2, 7], 9))
print(two_sum_sort([11, 15, 2, 7], 9))
print(two_sum_hash([11, 15, 2, 7], 9))
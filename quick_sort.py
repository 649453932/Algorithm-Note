'''选一个基准，将小于它的放在左边，大于它的放在右边，递归。'''


def quickSort(lis, start, end):
    if start < end:
        index = partion(lis, start, end)
        quickSort(lis, start, index - 1)
        quickSort(lis, index + 1, end)


def partion(lis, start, end):
    index = start - 1
    key = lis[end]
    for i in range(start, end):
        if lis[i] < key:
            index += 1
            lis[i], lis[index] = lis[index], lis[i]
    lis[end], lis[index + 1] = lis[index + 1], lis[end]
    return index + 1


a = [3, 4, 5, 1, 2, 6, 4]
print(a)
quickSort(a, 0, len(a) - 1)
print(a)

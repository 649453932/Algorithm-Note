'''选一个基准，将小于它的放在左边，大于它的放在右边，递归。'''
def quickSort(lis, start, end):
    if start < end:
        index = partion(lis, start, end)
        quickSort(lis, start, index - 1)
        quickSort(lis, index + 1, end)


def partion(lis, start, end):
    i = start - 1
    key = lis[end]
    for j in range(start, end):
        if lis[j] < key:
            i += 1
            lis[j], lis[i] = lis[i], lis[j]
    lis[i + 1], lis[end] = lis[end], lis[i + 1]
    return i + 1


a = [3, 4, 5, 1, 2, 6, 4]
print(a)
quickSort(a, 0, len(a) - 1)
print(a)

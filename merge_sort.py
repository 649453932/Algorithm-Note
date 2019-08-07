def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    num = int(len(lists) >> 1)
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return Merge(left, right)


def Merge(left, right):
    r, l = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += list(left[l:])
    result += list(right[r:])
    return result


a = [3, 4, 5, 1, 2, 6, 4]
print(a)
print(merge_sort(a))

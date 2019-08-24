
def merge_sort(lis):
    if lis is None or len(lis) < 2:
        return
    merge_process(lis, 0, len(lis) - 1)


def merge_process(lis, L, R):
    if L == R:
        return
    mid = (L + R) >> 1
    merge_process(lis, L, mid)
    merge_process(lis, mid + 1, R)
    merge(lis, L, mid, R)


def merge(lis, L, mid, R):
    tmp = []
    left = L
    right = mid + 1
    while left <= mid and right <= R:
        if lis[left] <= lis[right]:
            tmp.append(lis[left])
            left += 1
        else:
            tmp.append(lis[right])
            right += 1
    while left <= mid:
        tmp.append(lis[left])
        left += 1
    while right <= R:
        tmp.append(lis[right])
        right += 1
    for i in range(len(tmp)):
        lis[L + i] = tmp[i]


a = [1, 3, 5, 6, 4, 1]
print(a)
merge_sort(a)
print(a)

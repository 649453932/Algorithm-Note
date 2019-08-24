def heap_sort(lis):
    if lis is None or len(lis) < 2:
        return
    # 建立大根堆
    for i in range(len(lis)):
        heapInsert(lis, i)
    # 将首末位置互换，末位确定位置，对前面的位置调整为大根堆，循环此过程
    heap_size = len(lis)
    heapify(lis, heap_size - 1)


def heapInsert(lis, i):  # i位置及之前调整为大根堆(i位置是新放进来的元素)
    while lis[(i - 1) >> 1] < lis[i] and i != 0:
        lis[(i - 1) >> 1], lis[i] = lis[i], lis[(i - 1) >> 1]
        i = (i - 1) >> 1


def heapify(lis, i):
    while i > 0:
        lis[0], lis[i] = lis[i], lis[0]
        index = 0
        left = 1
        while left < i:
            largest = left + 1 if left + 1 < i and lis[left + 1] > lis[left] else left
            if lis[largest] <= lis[index]:
                break
            else:
                lis[largest], lis[index] = lis[index], lis[largest]
                index = largest
                left = index * 2 + 1
        i -= 1


a = [3, 4, 5, 1, 2, 6, 4]
print(a)
heap_sort(a)
print(a)


# # 使用库
# import heapq
# def heapsort(iterable):
#     h = []
#     for value in iterable:
#         heapq.heappush(h, value)
#     return [heapq.heappop(h) for i in range(len(h))]

# a = [3, 4, 5, 1, 2, 6, 4]
# print(a)
# print(heapsort(a))

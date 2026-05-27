import heapq

def insertion_sort(values):
    heap = values[:]
    heapq.heapify(heap)
    return [heapq.heappop(heap) for _ in range(len(heap))]

def n_smallest(values, n):
    return heapq.nsmallest(n, values)

def n_largest(values, n):
    return heapq.nlargest(n, values)

def median(values):
    s = sorted(values)
    mid = len(s) // 2
    return (s[mid - 1] + s[mid]) / 2 if len(s) % 2 == 0 else s[mid]

data = [5, 2, 8, 1, 9, 3, 7, 4, 6]
print(insertion_sort(data))
print(n_smallest(data, 3))
print(n_largest(data, 3))
print(median(data))

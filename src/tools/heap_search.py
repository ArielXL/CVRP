import heapq


def heap_search(bigArray, k):
    heap = []
    for item in bigArray:
        if len(heap) < k or item > heap[0]:
            if len(heap) == k:
                heapq.heappop(heap)
            heapq.heappush(heap, item)
    return heap
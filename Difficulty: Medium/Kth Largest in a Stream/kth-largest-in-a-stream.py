import heapq

class Solution:
    def kthLargest(self, arr, k):
        res = []
        minHeap = []

        for i in range(len(arr)):

            if len(minHeap) < k:
                heapq.heappush(minHeap, arr[i])

            elif arr[i] > minHeap[0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, arr[i])

            if len(minHeap) == k:
                res.append(minHeap[0])
            else:
                res.append(-1)

        return res
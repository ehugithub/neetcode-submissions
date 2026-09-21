class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []

        for right, num in enumerate(nums):
            heapq.heappush(heap, (-num, right))

            while heap and heap[0][1] <= right - k:
                heapq.heappop(heap)

            if right >= k - 1:
                res.append(-heap[0][0])

        return res
        
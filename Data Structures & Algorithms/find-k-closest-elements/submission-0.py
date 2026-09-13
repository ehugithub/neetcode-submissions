class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def findDist(a, b):
            return abs(a - b)
        dists = map(lambda y: findDist(y, x), arr)
        arr = zip(arr, dists)

        heap = []
        for num, dist in arr:
            heapq.heappush(heap, (dist, num))

        res = [heapq.heappop(heap)[1] for _ in range(k)]
        return sorted(res)

        
        
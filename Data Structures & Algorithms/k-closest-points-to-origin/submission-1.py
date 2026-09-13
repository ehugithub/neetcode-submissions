class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calcMagnitude(x, y):
            return x ** 2 + y ** 2
        dists = map(lambda x: calcMagnitude(x[0], x[1]), points)
        vecs = zip(points, dists)

        heap = []
        for vec in vecs:
            heapq.heappush(heap, (-vec[1], vec[0]))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [point for _, point in heap]
            

        
        
        
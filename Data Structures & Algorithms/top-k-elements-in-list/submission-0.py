class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        heap = [(freq, num) for num, freq in counts.items()]
        heapq.heapify(heap)

        return [p[1] for p in heapq.nlargest(k, heap)]
        
        
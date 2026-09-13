class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # using a max heap:
        counts = Counter(tasks)
        heap = [(-values, keys) for keys, values in counts.items()] 
        heapq.heapify(heap)
        q = deque()
        time = 0

        print(heap)

        while heap or q:
            if q and q[0][2] == time:
                task, freq, _ = q.popleft()
                heapq.heappush(heap, (freq, task))

            # want to greedily select the most frequent tasks first
            if heap:
                freq, task = heapq.heappop(heap)
                if freq < -1: 
                    q.append((task, freq + 1, time + n + 1))

            time += 1

        return time
        